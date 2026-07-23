\# Technology Stack



\## 1. Introduction



This document describes the technologies used in the Phishing Link Analyzer project. Each technology has been selected based on simplicity, performance, scalability, and its suitability for cybersecurity applications.



\---



\# 2. Programming Language



\## Python 3.12



\### Purpose



Python is the primary programming language used to develop the Phishing Link Analyzer.



\### Why We Chose Python



\- Python is one of the most popular programming languages in cybersecurity.

\- It provides a rich collection of libraries for networking, DNS, WHOIS, SSL, web scraping, and API integration.

\- Python has simple and readable syntax, making development faster.

\- It is widely used for automation and security tools.

\- It has a large community and excellent documentation.



\### Alternatives



\- Java

\- C#

\- Go



\---



\# 3. Backend Framework



\## FastAPI



\### Purpose



FastAPI is used to build the backend REST APIs for the project.



\### Why We Chose FastAPI



\- Lightweight and modern framework.

\- High performance.

\- Automatic API documentation.

\- Supports asynchronous programming.

\- Easy integration with Python libraries.



\### Alternatives



\- Flask

\- Django



\---



\# 4. Frontend Technologies



\## HTML



\### Purpose



Used to create the structure of the web pages.



\---



\## CSS



\### Purpose



Used to design and improve the appearance of the user interface.



\---



\## JavaScript



\### Purpose



Used to make the web application interactive, validate user input, communicate with the backend APIs, and display analysis results dynamically.



\---



\# 5. Python Libraries



\## httpx



\### Purpose



Used to send HTTP requests to external APIs such as VirusTotal and Google Safe Browsing.



\---



\## validators



\### Purpose



Used to validate user-entered URLs before analysis.



\---



\## python-whois



\### Purpose



Used to retrieve domain registration information.



\---



\## dnspython



\### Purpose



Used to perform DNS lookups.



\---



\## BeautifulSoup4



\### Purpose



Used to analyze website HTML content.



\---



\## python-dotenv



\### Purpose



Used to securely store API keys and environment variables.



\---



\## Pydantic



\### Purpose



Used for request validation and data models in FastAPI.



\---



\# 6. Development Tools



\## Visual Studio Code



\### Purpose



Primary code editor used for development.



\---



\## Git



\### Purpose



Used for version control and project history.



\---



\## GitHub



\### Purpose



Used to host the source code and manage the project.



\---



\## Postman



\### Purpose



Used for testing REST APIs.



\---



\# 7. External APIs



The project will integrate with the following external services.



\- VirusTotal API

\- Google Safe Browsing API (Optional)

\- PhishTank (Optional)



\---



\# 8. Future Technologies



The following technologies may be added in future versions.



\- Docker

\- GitHub Actions

\- PostgreSQL

\- Redis

\- Machine Learning

\- Browser Extension



\---



\# 9. Technology Summary



| Category | Technology |

|----------|------------|

| Programming Language | Python 3.12 |

| Backend Framework | FastAPI |

| Frontend | HTML, CSS, JavaScript |

| HTTP Client | httpx |

| URL Validation | validators |

| WHOIS Lookup | python-whois |

| DNS Lookup | dnspython |

| HTML Parsing | BeautifulSoup4 |

| Environment Variables | python-dotenv |

| Data Validation | Pydantic |

| Version Control | Git |

| Repository Hosting | GitHub |

| API Testing | Postman |

| Code Editor | Visual Studio Code |

