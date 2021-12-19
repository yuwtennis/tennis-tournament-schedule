""" Stateless Service """
from pytz import timezone
from google.auth.credentials import Credentials
from googleapiclient.discovery import build
from tournaments import ScheduleEntity


class CalendarService:

    @staticmethod
    def register_google_calendar(schedule: ScheduleEntity,
                                 credential: Credentials,
                                 calendar_id: str,
                                 calendar_tz: str = 'Asia/Tokyo'):
        """ Register google calendar """
        schedule = schedule.dump({})

        event = {
            'summary': schedule['title'],
            'start': {
                'dateTime': schedule['match_start'].astimezone(timezone(calendar_tz)).isoformat(),
                'timeZone': calendar_tz
            },
            'end': {
                'dateTime': schedule['match_end'].astimezone(timezone(calendar_tz)).isoformat(),
                'timeZone': calendar_tz
            }
        }

        service = build('calendar', 'v3', credentials=credential)
        service.events().insert(calendar_id=calendar_id, body=event)
