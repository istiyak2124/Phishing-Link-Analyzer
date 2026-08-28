from sqlalchemy import desc
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from backend.app.schemas.url_schema import URLRequest

# Database
from backend.app.models.database import Base, engine, get_db
from backend.app.models import scan_model
from backend.app.models.scan_model import Scan

# VirusTotal Service
from backend.app.services.virustotal_service import (
    submit_url,
    get_analysis_report,
)

# URL Analysis Services
from backend.app.services.url_service import (
    parse_url,
    check_https,
    check_ip_address,
    check_suspicious_keywords,
    check_url_length,
    check_at_symbol,
    check_hyphen,
    check_multiple_subdomains,
    check_shortened_url,
    check_suspicious_tld,
)

# Risk Engine
from backend.app.services.risk_engine import (
    calculate_risk_score,
    get_verdict,
)


# =============================================================================================
# FastAPI App
# =============================================================================================

app = FastAPI(
    title="Phishing Link Analyzer API",
    description="Backend API for analyzing phishing URLs.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create Database Tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "Welcome to Phishing Link Analyzer API",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "message": "API is working properly"
    }




@app.post("/analyze")
def analyze_url(
    data: URLRequest,
    db: Session = Depends(get_db)
):

    # -------------------------
    # Parse URL
    # -------------------------

    parsed_data = parse_url(str(data.url))

    # -------------------------
    # Local URL Analysis
    # -------------------------

    https_status = check_https(parsed_data)
    ip_status = check_ip_address(parsed_data)
    suspicious_keywords = check_suspicious_keywords(parsed_data)
    length_data = check_url_length(str(data.url))
    at_symbol = check_at_symbol(str(data.url))
    hyphen_used = check_hyphen(parsed_data)
    multiple_subdomains = check_multiple_subdomains(parsed_data)
    shortened_url = check_shortened_url(parsed_data)
    suspicious_tld = check_suspicious_tld(parsed_data)

    # -------------------------
    # VirusTotal Analysis
    # -------------------------

    analysis_id = submit_url(str(data.url))
    print("Analysis ID:", analysis_id)

    report = get_analysis_report(analysis_id)
    print("VirusTotal Report:", report)

    # -------------------------
    # Risk Engine
    # -------------------------

    risk_score = calculate_risk_score(
        https_enabled=https_status,
        ip_address_used=ip_status,
        is_long_url=length_data["is_long_url"],
        contains_at_symbol=at_symbol,
        contains_hyphen=hyphen_used,
        multiple_subdomains=multiple_subdomains,
        is_shortened_url=shortened_url,
        is_suspicious_tld=suspicious_tld,
        suspicious_keywords=suspicious_keywords,
        malicious_count=report["malicious"],
        suspicious_count=report["suspicious"],
    )

    verdict = get_verdict(risk_score)

    # -------------------------
    # Save Scan into Database
    # -------------------------

    new_scan = Scan(
        url=str(data.url),
        domain=parsed_data["domain"],
        risk_score=risk_score,
        verdict=verdict,
        malicious=report["malicious"],
        suspicious=report["suspicious"],
        harmless=report["harmless"],
        undetected=report["undetected"],
    )

    db.add(new_scan)
    db.commit()
    db.refresh(new_scan)

    # -------------------------
    # API Response
    # -------------------------

    return {
        "received_url": str(data.url),
        "url_details": parsed_data,
        "https_enabled": https_status,
        "ip_address_used": ip_status,
        "suspicious_keywords": suspicious_keywords,
        "url_length": length_data["url_length"],
        "is_long_url": length_data["is_long_url"],
        "contains_at_symbol": at_symbol,
        "contains_hyphen": hyphen_used,
        "multiple_subdomains": multiple_subdomains,
        "is_shortened_url": shortened_url,
        "is_suspicious_tld": suspicious_tld,
        "risk_score": risk_score,
        "verdict": verdict,
        "virustotal": report,
        "status": "Received Successfully"
    }


@app.get("/history")
def get_scan_history(
    db: Session = Depends(get_db)
):
    scans = (
        db.query(Scan)
        .order_by(desc(Scan.id))
        .all()
    )

    return [
        {
            "id": scan.id,
            "url": scan.url,
            "domain": scan.domain,
            "risk_score": scan.risk_score,
            "verdict": scan.verdict,
            "malicious": scan.malicious,
            "suspicious": scan.suspicious,
            "harmless": scan.harmless,
            "undetected": scan.undetected,
            "created_at": scan.created_at,
        }
        for scan in scans
    ]

@app.get("/history/{scan_id}")
def get_scan_by_id(
    scan_id: int,
    db: Session = Depends(get_db)
):
    scan = (
        db.query(Scan)
        .filter(Scan.id == scan_id)
        .first()
    )

    if scan is None:
        raise HTTPException(
            status_code=404,
            detail="Scan not found."
        )

    return {
        "id": scan.id,
        "url": scan.url,
        "domain": scan.domain,
        "risk_score": scan.risk_score,
        "verdict": scan.verdict,
        "malicious": scan.malicious,
        "suspicious": scan.suspicious,
        "harmless": scan.harmless,
        "undetected": scan.undetected,
        "created_at": scan.created_at,
    }


@app.delete("/history/{scan_id}")
def delete_scan(
    scan_id: int,
    db: Session = Depends(get_db)
):
    scan = (
        db.query(Scan)
        .filter(Scan.id == scan_id)
        .first()
    )

    if scan is None:
        raise HTTPException(
            status_code=404,
            detail="Scan not found."
        )

    db.delete(scan)
    db.commit()

    return {
        "message": f"Scan with ID {scan_id} deleted successfully."
    }

@app.delete("/history")
def delete_all_scans(
    db: Session = Depends(get_db)
):
    deleted_rows = db.query(Scan).delete()

    db.commit()

    return {
        "message": f"{deleted_rows} scan(s) deleted successfully."
    }