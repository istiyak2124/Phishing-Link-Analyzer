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
):
    score = 0

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

    score += len(suspicious_keywords) * 5

    return score

def get_verdict(score: int):
    if score >= 60:
        return "Phishing"

    elif score >= 30:
        return "Suspicious"

    else:
        return "Safe"