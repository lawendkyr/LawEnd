import requests
from bs4 import BeautifulSoup
from urllib.parse import quote, urlparse, parse_qs, unquote


def clean_url(url):
    if url.startswith("//"):
        url = "https:" + url

    parsed = urlparse(url)

    if "duckduckgo.com" in parsed.netloc:
        query = parse_qs(parsed.query)

        if "uddg" in query:
            return unquote(query["uddg"][0])

    return url


def search_web(query):
    url = "https://html.duckduckgo.com/html/?q=" + quote(query)

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 "
            "Chrome/140.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        response.raise_for_status()

    except requests.RequestException as e:
        print(f"[ERROR] Suche fehlgeschlagen: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    for result in soup.select(".result"):

        link = result.select_one(".result__a")

        if not link:
            continue

        title = link.get_text(" ", strip=True)

        raw_url = link.get("href", "")
        real_url = clean_url(raw_url)

        snippet_element = result.select_one(".result__snippet")

        snippet = ""

        if snippet_element:
            snippet = snippet_element.get_text(
                " ",
                strip=True
            )

        results.append({
            "title": title,
            "url": real_url,
            "snippet": snippet
        })

    return results
