# AI Learning Digest

A Python-based AI news aggregator that fetches the latest Artificial Intelligence news articles using the NewsAPI.

## Features

- Fetches recent AI-related news articles
- Displays article title, description, source, and publication date
- Uses environment variables for secure API key management
- Simple command-line interface
- Beginner-friendly implementation

## Tech Stack

- Python
- Requests
- NewsAPI
- Python-dotenv

## Project Structure

```text
AI-LEARNING-DIGEST/
│
├── .env.example
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

## Setup

Clone the repository:

```bash
git clone <repository-url>
cd AI-LEARNING-DIGEST
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
NEWSAPI_KEY=your_api_key_here
```

Get a free API key from:
https://newsapi.org

Run the application:

```bash
python main.py
```

## Example Output

- Article Title
- Description
- Source
- Published Date
- URL

## Future Improvements

- GUI interface
- Streamlit deployment
- News filtering by category
- Email newsletter support
- AI-powered article summarization
