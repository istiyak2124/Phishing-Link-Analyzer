def calculate_risk_score(
    https_enabled: bool,
    ip_address_used: bool,
    is_long_url: bool,
    contains_at_symbol: bool,
    contains_hyphen: bool,
    multiple_subdomains: bool,
    is_shortened_url: bool,
    is_suspicious_tld: bool,
    suspicious_keywords: list,
    malicious_count: int,
    suspicious_count: int,
):
    score = 0

    # -------------------------
    # Local URL Analysis Score
    # -------------------------

    if not https_enabled:
        score += 10

    if ip_address_used:
        score += 25

    if is_long_url:
        score += 5

    if contains_at_symbol:
        score += 20

    if contains_hyphen:
        score += 5

    if multiple_subdomains:
        score += 10

    if is_shortened_url:
        score += 20

    if is_suspicious_tld:
        score += 15

    # Suspicious Keywords
    score += len(suspicious_keywords) * 5

    # -------------------------
    # VirusTotal Score
    # -------------------------

    # Multiple detections increase confidence.
    # A single detection is given a small score
    # because one engine can sometimes produce a false positive.

    if malicious_count >= 5:
        score += 40

    elif malicious_count >= 3:
        score += 25

    elif malicious_count >= 1:
        score += 10

    if suspicious_count >= 5:
        score += 20

    elif suspicious_count >= 3:
        score += 10

    elif suspicious_count >= 1:
        score += 5

    # -------------------------
    # Keep Score Between 0-100
    # -------------------------

    return min(score, 100)


def get_verdict(score: int):

    if score >= 60:
        return "Phishing"

    elif score >= 30:
        return "Suspicious"

    else:
        return "Safe"