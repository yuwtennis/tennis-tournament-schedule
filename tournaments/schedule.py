""" Schedule Module """
import urllib.request as rq
from bs4 import BeautifulSoup
import pandas as pd
from marshmallow import Schema, fields
from tournaments.helper import parse_jpn_date


class ScheduleEntity(Schema):
    venue_name = fields.Str()
    match_type = fields.Str()
    match_date = fields.DateTime()
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

        for index, row in df[table[spec['match_type_jpn']]].loc[1:].iterrows():
            yield ScheduleEntity.load({
                'venue_name': inst['venue_name'],
                'match_type': inst['match_type'],
                'match_date': parse_jpn_date(row[0], row[3]),
                'availability': row[5]})
