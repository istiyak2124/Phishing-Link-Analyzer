import httpx

from backend.app.core.config import VIRUSTOTAL_API_KEY


VT_SUBMIT_URL = "https://www.virustotal.com/api/v3/urls"


def submit_url(url: str):
    """
    Submit a URL to VirusTotal for analysis.
    """

    headers = {
        "x-apikey": VIRUSTOTAL_API_KEY
    }

    data = {
        "url": url
    }

    response = httpx.post(
        VT_SUBMIT_URL,
        headers=headers,
        data=data,
        timeout=30
    )

    response.raise_for_status()
    result = response.json()
    analysis_id = result["data"]["id"]
    return analysis_id