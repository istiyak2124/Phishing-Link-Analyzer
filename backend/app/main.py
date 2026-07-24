from fastapi import FastAPI
from backend.app.schemas.url_schema import URLRequest

# VirusTotal Service
from backend.app.services.virustotal_service import submit_url

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

app = FastAPI(
    title="Phishing Link Analyzer API",
    description="Backend API for analyzing phishing URLs.",
    version="1.0.0"
)


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
def analyze_url(data: URLRequest):

    # Parse URL
    parsed_data = parse_url(str(data.url))

    # URL Checks
    https_status = check_https(parsed_data)
    ip_status = check_ip_address(parsed_data)
    suspicious_keywords = check_suspicious_keywords(parsed_data)
    length_data = check_url_length(str(data.url))
    at_symbol = check_at_symbol(str(data.url))
    hyphen_used = check_hyphen(parsed_data)
    multiple_subdomains = check_multiple_subdomains(parsed_data)
    shortened_url = check_shortened_url(parsed_data)
    suspicious_tld = check_suspicious_tld(parsed_data)

    # Temporary VirusTotal Test
    analysis_id = submit_url(str(data.url))

    print("Analysis ID:", analysis_id)

    # Risk Engine
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
    )

    verdict = get_verdict(risk_score)

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
        "status": "Received Successfully"
    }