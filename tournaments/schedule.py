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

    @classmethod
    def scrape_schedule_of_mitg_by_spec(cls, spec: Schema):

        inst = spec.dump({})

        resp = rq.urlopen(inst['url'])
        soup = BeautifulSoup(resp.read().decode('utf-8'), 'html.parser')

        table = {s.string: idx for idx, s in
                 enumerate(soup.find_all('p', style='text-align: center;'))}

        df = pd.read_html(inst['url'])

        for index, row in df[table[spec['match_type']]].loc[1:].iterrows():
            start = parse_jpn_date(row[0], row[3])

            # ToDo Factory per calendar better
            yield ScheduleEntity.load({
                'title': f'{inst["venue_name"]} {inst["match_type"]} {inst["level"]}',
                'match_start': start,
                'match_end': start+timedelta(hours=inst['duration_in_hours']),
                'availability': row[5]})
