""" Schedule Module """
import urllib.request as rq
from datetime import timedelta

from bs4 import BeautifulSoup
import pandas as pd
from marshmallow import Schema, fields
from tournaments.helper import parse_jpn_date


class ScheduleEntity(Schema):
    title = fields.Str()
    match_start = fields.DateTime()
    match_end = fields.DateTime()
    availability = fields.Str()


class ScheduleRepository:

    @staticmethod
    def scrape_schedule(venue_name, tournament_facts: Schema):
        """
        Scrape schedule from website

        Parameters
        ----------
        venue_name
        tournament_facts

        Yields
        -------
        ScheduleEntity

        """

        inst = tournament_facts.dump({})

        if venue_name == 'minami_ichikawa_tennis_garden':
            resp = rq.urlopen(inst['url'])
            soup = BeautifulSoup(resp.read().decode('utf-8'), 'html.parser')

            table = {s.string: idx for idx, s in
                     enumerate(soup.find_all('p', style='text-align: center;'))
                     }

            df = pd.read_html(inst['url'])

            for index, row in df[table[inst['match_type']]].loc[1:].iterrows():
                start = parse_jpn_date(row[0], row[3])

                # ToDo Factory per calendar better
                yield ScheduleEntity.load({
                    'title': f'{inst["venue_name"]} {inst["match_type"]} {inst["level"]}',
                    'match_start': start,
                    'match_end': start+timedelta(hours=inst['duration_in_hours']),
                    'availability': row[5]})
        else:
            raise ValueError
