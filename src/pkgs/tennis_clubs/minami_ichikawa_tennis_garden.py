
from config import *
from tennis_club import TennisClub
from scraper import Scraper
from extracter import Extracter

class MinamiIchikawaTennisGarden(TennisClub):

    def __init__(self):
        super().__init__(TENNIS_CLUB_1)

    """
    Display the result
    """
    def display():
        super().display(self._run())

    """
    Run workflow
    """ 
    def _run():
        for u in self.yaml['urls']:

            return [ self._extract(i, u['url']) for i in self._find_indexes(u['filter'])]

    """
    Extract schedule according to tournament
    """
    def _extract(self, target, url):

        return Extracter.extract_by_dataframe(target, url)

    """
    Scrape web site and return result
    """
    def _scrape(self, key, val):

        return Scraper.scrape_by_identifier(key, val)

    """
    Return index number of corresponding tournament
    """
    def _find_indexes(self, tournament_list):
        scraped = self._scrape()

        return { t: scraped.index(d) for t in tournament_list if t in scraped }
