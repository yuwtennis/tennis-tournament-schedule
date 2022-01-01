""" Stateless Service """
from typing import List
from datetime import timedelta
from hashlib import sha256
import logging
from tournaments.helper import is_event_registered

LOGGER = logging.getLogger(__name__)


class CalendarService:

    @staticmethod
    def register_google_calendar(service, calendar_id, schedules: List):
        """ Register events to specified google calendar """

        for schedule in schedules:

            inst = schedule.dump({})

            event = {
                'summary': f'{inst["match_type"]} {inst["venue_name"]}',
                'start': {
                    'dateTime': inst['match_date'].isoformat(),
                    'timeZone': inst['match_date'].zone,
                },
                'end': {
                    'dateTime':
                        (inst['match_date'] + timedelta(hours=5)).isoformat(),
                    'timeZone': inst['match_date'].zone,
                }
            }

            event['id'] = sha256(f'{event["summary"]}').hexdigest()

            try:
                if is_event_registered(event['id']):
                    service.events()\
                        .update(
                            calendarId=calendar_id,
                            eventId=event['id'],
                            body=event).execute()
                else:
                    service.events()\
                        .insert(
                            calendarId=calendar_id,
                            body=event).execute()

            except Exception:
                LOGGER.error('Failed to register event. %s', event['summary'])

            LOGGER.info('Completed event registering.')
