from urllib.parse import urlparse
import ipaddress

SUSPICIOUS_KEYWORDS = [
    "login",
    "verify",
    "update",
    "secure",
    "account",
    "bank",
    "signin",
    "confirm",
    "password",
]

SHORTENING_SERVICES = [
    "bit.ly",
    "tinyurl.com",
    "t.co",
    "goo.gl",
    "is.gd",
    "buff.ly",
    "ow.ly",
    "rb.gy",
    "cutt.ly",
    "rebrand.ly"
]

SUSPICIOUS_TLDS = [
    ".xyz",
    ".top",
    ".click",
    ".zip",
    ".country",
    ".gq",
    ".tk"
]



def parse_url(url: str):
    parsed_url = urlparse(url)

    return {
        "scheme": parsed_url.scheme,
        "domain": parsed_url.hostname,
        "path": parsed_url.path,
        "query": parsed_url.query,
    }

def check_https(url_data: dict):
    return url_data["scheme"] == "https"


def check_ip_address(url_data: dict):
    try:
        ipaddress.ip_address(url_data["domain"])
        return True
    except ValueError:
        return False
    
def check_suspicious_keywords(url_data: dict):
    text = (url_data["domain"] + url_data["path"]).lower()

    found_keywords = []

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in text:
            found_keywords.append(keyword)

    return found_keywords

def check_url_length(url: str):
    length = len(url)

    return {
            "url_length": length,
            "is_long_url": length > 75
    }

def check_at_symbol(url: str):
    return "@" in url

def check_hyphen(url_data: dict):
    return "-" in url_data["domain"]

def check_multiple_subdomains(url_data: dict):
    domain = url_data["domain"]
    dot_count = domain.count(".")
    return dot_count >= 3

def check_shortened_url(url_data: dict):
    domain = url_data["domain"].lower()

    return domain in SHORTENING_SERVICES

def check_suspicious_tld(url_data: dict):
    domain = url_data["domain"].lower()

    for tld in SUSPICIOUS_TLDS:
        if domain.endswith(tld):
            return True

    return False