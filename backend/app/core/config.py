from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Read VirusTotal API Key
VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
