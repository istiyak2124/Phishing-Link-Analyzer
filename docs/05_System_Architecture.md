\# System Architecture



\## 1. Introduction



The Phishing Link Analyzer follows a modular architecture where each component has a specific responsibility. The system is designed to keep the code organized, maintainable, and easy to extend in future versions.



The user interacts with the application through a web interface. The request is processed by the FastAPI backend, where different analysis modules examine the given URL. The results are combined by the Risk Scoring Engine and returned to the user.



\---



\# 2. High-Level Architecture



```

+----------------------+

|       User           |

+----------+-----------+

&#x20;          |

&#x20;          | Enter URL

&#x20;          v

+----------------------+

|      Frontend        |

| HTML + CSS + JS      |

+----------+-----------+

&#x20;          |

&#x20;          | HTTP Request

&#x20;          v

+----------------------+

|    FastAPI Backend   |

+----------+-----------+

&#x20;          |

&#x20;          |

&#x20;          +----------------------------+

&#x20;          |                            |

&#x20;          v                            v

+------------------+          +------------------+

| URL Validator    |          | URL Normalizer   |

+------------------+          +------------------+

&#x20;          |

&#x20;          v

+----------------------+

| Feature Extraction   |

+----------+-----------+

&#x20;          |

&#x20;          +-------------------------------------------+

&#x20;          |           |           |          |         |

&#x20;          v           v           v          v         v

&#x20;      WHOIS        DNS Lookup    SSL    Threat Intel  Website Analysis

&#x20;                                       (VirusTotal)

&#x20;          |

&#x20;          +---------------------------+

&#x20;                                      |

&#x20;                                      v

&#x20;                         +-------------------------+

&#x20;                         | Risk Scoring Engine     |

&#x20;                         +-----------+-------------+

&#x20;                                     |

&#x20;                                     v

&#x20;                         +-------------------------+

&#x20;                         | Analysis Report         |

&#x20;                         | Risk Score              |

&#x20;                         | Recommendation          |

&#x20;                         +-----------+-------------+

&#x20;                                     |

&#x20;                                     v

&#x20;                              Display to User

```



\---



\# 3. Component Description



\### User



The user enters a website URL that needs to be analyzed.



\---



\### Frontend



The frontend collects the URL from the user and sends it to the FastAPI backend.



\---



\### FastAPI Backend



Acts as the central controller of the application. It receives the request and coordinates all analysis modules.



\---



\### URL Validator



Checks whether the entered URL is valid.



\---



\### URL Normalizer



Converts the URL into a standard format before analysis.



\---



\### Feature Extraction



Extracts useful characteristics from the URL that help identify suspicious behavior.



\---



\### WHOIS Module



Retrieves domain registration information.



\---



\### DNS Lookup Module



Collects DNS records related to the domain.



\---



\### SSL Analysis Module



Checks SSL certificate information.



\---



\### Threat Intelligence Module



Uses external services such as VirusTotal to determine whether the URL has already been reported as malicious.



\---



\### Website Analysis Module



Examines the webpage and gathers additional information such as redirects, forms, and page content.



\---



\### Risk Scoring Engine



Combines all collected information and calculates the final risk score.



\---



\### Analysis Report



Generates a detailed report including:



\- Risk Score

\- Risk Level

\- Reasons

\- Recommendations



\---



\# 4. Request Flow



The overall workflow of the application is:



1\. User enters a URL.

2\. Frontend sends the request to the FastAPI backend.

3\. The backend validates and normalizes the URL.

4\. Multiple analysis modules examine the URL.

5\. The Risk Scoring Engine calculates the final score.

6\. The report is generated.

7\. The result is displayed to the user.



\---



\# 5. Design Principles



The system is designed using the following principles:



\- Modular Architecture

\- Separation of Concerns

\- Scalability

\- Maintainability

\- Reusability

\- Clean Code Practices

