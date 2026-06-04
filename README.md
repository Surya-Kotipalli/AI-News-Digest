# AI News Digest

An automated Python-based news aggregation application that retrieves and displays the latest Artificial Intelligence news articles using the NewsAPI. The project demonstrates API integration, environment variable management, data retrieval, and structured information presentation through a command-line interface.

---

## Overview

AI News Digest fetches real-time AI-related news articles from trusted online sources and presents them in a clean, readable format. The application is designed as a lightweight news monitoring tool and serves as a practical example of working with REST APIs in Python.

---

## Features

- Retrieves the latest Artificial Intelligence news articles
- Displays article title, description, source, publication date, and URL
- Integrates with NewsAPI for real-time data retrieval
- Uses environment variables for secure API key management
- Clean command-line output formatting
- Simple and extensible architecture

---

## Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| API Integration | NewsAPI |
| HTTP Requests | Requests |
| Environment Management | Python-dotenv |
| Version Control | Git & GitHub |

---

## Project Structure

```text
AI-News-Digest/
│
├── Screenshots/
│
├── .env.example
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Surya-Kotipalli/AI-News-Digest.git
cd AI-News-Digest
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root directory:

```env
NEWSAPI_KEY=your_api_key_here
```

Get your API key from:

https://newsapi.org

---

## Usage

Run the application:

```bash
python main.py
```

The application fetches and displays the most recent AI-related news articles along with their source, publication date, description, and article link.

---

## Sample Output

```text
Article 1

Title       : OpenAI releases new AI model
Description : Latest advancements in AI capabilities...
Source      : TechCrunch
Published   : 2026-06-03
URL         : https://example.com/article
```

---

## Learning Outcomes

This project demonstrates:

- Working with REST APIs in Python
- JSON data parsing and processing
- Secure handling of API credentials
- Environment variable management
- Command-line application development
- Project structuring and documentation practices

---

## Future Improvements

- Category-based news filtering
- Keyword search functionality
- Email-based news digest delivery
- AI-powered article summarization
- Streamlit web interface
- Scheduled automated news reports

---

## Author

**Surya Teja**

Aspiring Data Scientist interested in AI, Machine Learning, Analytics, and Intelligent Systems Development.

GitHub: https://github.com/Surya-Kotipalli
