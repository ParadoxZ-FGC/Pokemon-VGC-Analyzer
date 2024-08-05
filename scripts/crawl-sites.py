# Crawl resource sites : Prints out sub-links for other scripts to pull from, writes urls associated with specified regulation to a .txt

# pip install requests bs4
import logging
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s", level=logging.INFO)

reg = "G"

class Crawler:
    def __init__(self, urls=None):
        if urls is None:
            urls = []
        self.visited_urls = []
        self.urls_to_visit = urls

    def download_url(self, url):    # Returns txt for specified URL
        return requests.get(url).text

    def get_linked_urls(self, url, html):   # Scans current URL page for sublinks
        soup = BeautifulSoup(html, "html.parser")
        for link in soup.find_all("a"):
            path = link.get("href")
            if path and path.startswith("/"):
                path = urljoin(url, path)
            yield path

    def add_url_to_visit(self, url):    # Adds sublinks found on a URL to urls_to_vist
        if url not in self.visited_urls and url not in self.urls_to_visit:
            self.urls_to_visit.append(url)

    def crawl(self, url):   # Crawls specified 
        html = self.download_url(url)
        for url in self.get_linked_urls(url, html):
            self.add_url_to_visit(url)

    def run(self):  # Crawls specified URLs and sublinks until there are no more unvisited links
        while self.urls_to_visit:
            url = self.urls_to_visit.pop(0)
            logging.info(f"Crawling: {url}")
            try:
                self.crawl(url)
                with open("..data/site-dumps/current_crawl_page.txt", "w", encoding="utf-8") as current:
                    current.write(requests.get(url).text)
                current.close()
                for line in open("..data/site-dumps/current_crawl_page.txt", "r", encoding="utf-8").readlines():
                    if f"VGC Regulation Set {reg}" in line:
                        with open(f"..data/site-dumps/reg-{reg.lower()}_tourney_urls.txt", "a", encoding="utf-8") as reg_urls:
                            reg_urls.write(url + "\n")
                        reg_urls.close()
            except Exception:
                logging.exception(f"Failed to crawl: {url}")
            finally:
                self.visited_urls.append(url)


if __name__ == "__main__":
    Crawler(urls=["https://victoryroadvgc.com/2024-season-calendar/", f"https://www.smogon.com/dex/sv/formats/vgc24-regulation-{reg.lower()}/"]).run()
