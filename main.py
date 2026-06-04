"""
AI News Reader (beginner project)

What this script does:
- Calls the NewsAPI "Everything" endpoint
- Searches for Artificial Intelligence articles
- Prints the top 5 results: Title, Source, URL

Before you run it:
1) Create a free API key at https://newsapi.org/
2) Create a '.env' file in the project root directory.
3) Add your NewsAPI key inside the '.env' file: NEWSAPI_KEY=your_actual_api_key_here
"""
import os
import sys

import requests
from dotenv import load_dotenv
load_dotenv()

NEWSAPI_EVERYTHING_URL = "https://newsapi.org/v2/everything"


def get_api_key():
    api_key = os.getenv("NEWSAPI_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set the NEWSAPI_KEY environment variable.")
    return api_key


def fetch_ai_articles(api_key, topic, limit):
    """
    Fetch articles related to Artificial Intelligence.

    Returns:
        A list of article dictionaries (each dict has keys like: title, url, source, etc.)
    """
    # 'q' is the search query. We keep it simple and broad.
    # 'language' filters to English results.
    # 'pageSize' tells NewsAPI how many results we want back.
    print(f"Fetching up to {limit} articles about '{topic}' from NewsAPI...")
    params = {
        "q": topic,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": limit,
    }

    # NewsAPI accepts the API key via an Authorization-style header: X-Api-Key.
    headers = {"X-Api-Key": api_key}

    # Make the HTTP request.
    response = requests.get(NEWSAPI_EVERYTHING_URL, params=params, headers=headers, timeout=20)

    # If the server returns a 4xx/5xx status, raise an error so we can handle it cleanly.
    response.raise_for_status()

    # Convert the JSON response into a Python dictionary.
    data = response.json()

    # NewsAPI includes a 'status' field in the JSON body too.
    if data.get("status") != "ok":
        # 'message' typically explains what's wrong (invalid key, rate limit, etc.)
        message = data.get("message", "Unknown error from NewsAPI.")
        raise RuntimeError(f"NewsAPI error: {message}")

    # 'articles' is the list we care about.
    return data.get("articles", [])


def print_articles(articles: list[dict]) -> None:
    """
    Print title, source, and URL for each article.
    """
    if not articles:
        print("No articles found. Try again later or change the search query.")
        return

    for i, article in enumerate(articles, start=1):
        # Each article is a dictionary. Some fields can be missing, so we use .get().
        title = article.get("title") or "(No title)"
        url = article.get("url") or "(No url)"
        description = article.get("description") or "(No description)"
        published_at = article.get("publishedAt") or "(No publish date)"
        # 'source' is another dictionary like: {"id": "...", "name": "BBC News"}
        source = article.get("source") or {}
        source_name = source.get("name") or "(Unknown source)"

        print(f"\nArticle {i}")
        print(f"Title : {title}")
        print(f"Description: {description}")
        print(f"Published At: {published_at}")
        print(f"Source: {source_name}")
        print(f"URL   : {url}")


def main() -> None:
    # Startup validation: Verify that NEWSAPI_KEY exists and is loaded correctly.
    try:
        api_key = get_api_key()
    except ValueError as e:
        print(f"Startup Validation Error:\n{e}")
        sys.exit(1)

    try:
        # Fetch AI-related articles from NewsAPI.
        topic = input("Enter a topic for news search: ")
        limit = int(input("Enter the number of articles to fetch (1-100): "))
        articles = fetch_ai_articles(
            api_key,
            topic,
            limit
        )
    except requests.exceptions.Timeout:
        print("Request timed out. Check your internet connection and try again.")
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        # This often happens for invalid API key (401) or rate limit (429).
        print(f"HTTP error calling NewsAPI: {e}")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        # Any other requests-related error (DNS issues, connection errors, etc.)
        print(f"Network error calling NewsAPI: {e}")
        sys.exit(1)
    except RuntimeError as e:
        # This catches the JSON 'status' != 'ok' case.
        print(str(e))
        sys.exit(1)
        
    
    # Print the results.
    print_articles(articles)


if __name__ == "__main__":
    main()

