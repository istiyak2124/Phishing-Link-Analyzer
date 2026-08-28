import httpx
import time


from backend.app.core.config import VIRUSTOTAL_API_KEY


VT_SUBMIT_URL = "https://www.virustotal.com/api/v3/urls"
VT_ANALYSIS_URL = "https://www.virustotal.com/api/v3/analyses"


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


def get_analysis_report(analysis_id: str):
    """
    Fetch completed analysis report from VirusTotal.
    """

    headers = {
        "x-apikey": VIRUSTOTAL_API_KEY
    }

    for _ in range(15):

        response = httpx.get(
            f"{VT_ANALYSIS_URL}/{analysis_id}",
            headers=headers,
            timeout=30
        )

        response.raise_for_status()

        result = response.json()

        status = result["data"]["attributes"]["status"]

        print("Current Status:", status)


        if status in ["completed", "failed"]:

            stats = result["data"]["attributes"].get("stats", {})

            return {
                "malicious": stats.get("malicious", 0),
                "suspicious": stats.get("suspicious", 0),
                "harmless": stats.get("harmless", 0),
                "undetected": stats.get("undetected", 0),
            }

        time.sleep(2)

    return {
        "malicious": 0,
        "suspicious": 0,
        "harmless": 0,
        "undetected": 0,
    }