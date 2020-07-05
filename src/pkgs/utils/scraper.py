
import urllib.request as rq
from bs4 import BeautifulSoup

class Scraper:
    """
    Simple wrapper to scrape web page using identifier.
    """
    @staticmethod
    def scrape_by_identifier(url, identifier, identifier_str):

        resp = rq.urlopen(url)
        soup = BeautifulSoup(resp.read().decode('utf-8'), 'html.parser')

        if identifier == 'style':
            return [ s.string for s in soup.find_all(style=identifier_str) ]

        else:
            raise(NameError("Tournamet {} not found".format(identifier_str)))

