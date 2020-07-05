
from pkgs.config import *
from pkgs.tennis_club import TennisClub
from pkgs.utils.scraper import Scraper
from pkgs.utils.extracter import Extracter

class MinamiIchikawaTennisGarden(TennisClub):

    def __init__(self):
        super().__init__(TENNIS_CLUB_1)

    """
    Display the result
    """
    def notify_to_console(self):
        msgs = [ DISPLAY_FORMAT.format(k, d, s) for k, v in self._run().items() for d, s in v.items() ]

        super().notify_to_console(msgs)

    """
    Run workflow
    """ 
    def _run(self):

        schedule = dict()

        for u in self.yaml['urls']:
            scraped = self._scrape(u['url'],
                self.yaml['identifier']['key'],
                self.yaml['identifier']['val'])

            idx_list = self._find_indexes(u['filter'], scraped)

            schedule.update({ k: self._extract(v, u['url']) for k, v in idx_list.items() })

        return schedule

    """
    Extract schedule according to tournament
    """
    def _extract(self, target, url):

        return Extracter.extract_by_df(target, url)

    """
    Scrape web site and return result
    """
    def _scrape(self, url, key, val):

        return Scraper.scrape_by_identifier(url, key, val)

    """
    Return index number of corresponding tournament
    """
    def _find_indexes(self, tournament_list, scraped):

        return { t: scraped.index(t) for t in tournament_list if t in scraped }
