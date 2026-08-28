# 🛡️ Phishing Link Analyzer

A modern web application that analyzes URLs for potential phishing threats using intelligent URL inspection, risk scoring, and VirusTotal integration.

The application helps users quickly determine whether a website appears safe, suspicious, or potentially malicious before visiting it.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)
![VirusTotal](https://img.shields.io/badge/VirusTotal-API-007ACC)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- 🔍 Intelligent URL Analysis
- 🛡️ Phishing Detection
- 🌐 VirusTotal API Integration
- 📊 Risk Score Calculation
- 📜 Scan History
- 🗑️ Delete Scan History
- 📈 Statistics Dashboard
- ⚡ Enter Key Support
- 📱 Fully Responsive Design
- 🎨 Modern Dark User Interface

---

## 📸 Preview
![alt text](image.png)

> Add screenshots of the application here.

Example:

- Home Page
- URL Analysis Result
- Scan History
- Mobile Responsive View

---

## 🛠️ Tech Stack

### Frontend

- HTML5
- CSS3
- JavaScript (ES6)

### Backend

- Python
- FastAPI
- SQLAlchemy

### Database

- SQLite

### External API

- VirusTotal API

### Development Tools

- VS Code
- Git
- GitHub
- Postman

---

## 📂 Project Structure

```text
Phishing-Link-Analyzer/
│
├── backend/
│   └── app/
│       ├── database/
│       ├── models/
│       ├── routes/
│       ├── schemas/
│       ├── services/
│       └── main.py
│
├── frontend/
│   ├── assets/
│   ├── css/
│   ├── js/
│   └── index.html
│
├── docs/
├── screenshots/
├── tests/
├── README.md
├── LICENSE
├── requirements.txt
└── .env
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Phishing-Link-Analyzer.git
```

### 2. Navigate to the Project

```bash
cd Phishing-Link-Analyzer
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure VirusTotal API Key

Create a `.env` file inside the project root.

```env
VIRUSTOTAL_API_KEY=YOUR_API_KEY
```

### 7. Start the Backend

```bash
python -m uvicorn backend.app.main:app --reload
```

### 8. Run the Frontend

Open `frontend/index.html` using **Live Server** in Visual Studio Code.

---

## 💻 Usage

1. Enter a website URL.
2. Click **Analyze** or press **Enter**.
3. Wait for the analysis to complete.
4. Review the verdict and risk score.
5. Check VirusTotal statistics.
6. View previous scans in the history section.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API Home |
| GET | `/health` | Health Check |
| POST | `/analyze` | Analyze URL |
| GET | `/history` | Get Scan History |
| GET | `/history/{id}` | Get Scan by ID |
| DELETE | `/history/{id}` | Delete Single Scan |
| DELETE | `/history` | Delete All Scan History |

---

## 🔮 Future Improvements

- User Authentication
- Export Scan Reports
- PDF Report Generation
- Docker Support
- Multi-language Support
- Advanced Threat Intelligence
- Domain Reputation Analysis
- WHOIS Information
- DNS Lookup
- Email Phishing Detection

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Istiyak Ahmed**

Cyber Security Student

GitHub: https://github.com/YOUR_GITHUB_USERNAME

---

⭐ If you found this project useful, consider giving it a star on GitHub.