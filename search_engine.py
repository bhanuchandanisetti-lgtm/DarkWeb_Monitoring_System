import requests
from bs4 import BeautifulSoup
from config import TOR_PROXY, REQUEST_TIMEOUT

def query_search_engine(engine_url, query):
    try:
        r = requests.get(f"{engine_url}/search?q={query}",
                         proxies=TOR_PROXY,
                         timeout=REQUEST_TIMEOUT)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "lxml")
        links = set()
        for a in soup.find_all("a", href=True):
            if ".onion" in a["href"]:
                links.add(a["href"])
        return list(links)
    except Exception:
        return []
