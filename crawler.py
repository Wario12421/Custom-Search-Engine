import requests
from bs4 import BeautifulSoup
import json
import time
specific_links = [
"https://en.wikipedia.org/wiki/Artificial_intelligence",
    "https://en.wikipedia.org/wiki/Machine_learning",
    # Add any additional specific links here
]

def crawl_specific(links):
    visited = set()
    for url in links:
        if url in visited:
            continue
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            visited.add(url)
            print(f"Crawling: {url}")
            time.sleep(1)
        except Exception as e:
            print(f"Error crawling {url}: {e}")
            continue
    return list(visited)

if __name__ == "__main__":
    crawled_urls = crawl_specific(specific_links)
    with open("urls_specific.json", "w") as f:
        json.dump(crawled_urls, f)