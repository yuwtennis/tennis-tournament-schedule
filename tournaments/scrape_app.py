""" Application layer """
import os
from importlib import import_module
import google.auth
from tournaments.schedule import ScheduleRepository
from tournaments.calendar import CalendarService
from tournaments.policies import CalendarPolicy


def client():
    """ """
    venue_module_name = os.getenv('VENUE_MODULE_NAME', 'minami_ichikawa_tennis_garden')
    tournament_spec_name = os.getenv('TOURNAMENT_SPEC_NAME', 'SemiOpenSingles')
    calendar_type = os.getenv('CALENDAR_TYPE', 'google_calendar')
    calendar_id = os.getenv('CALENDAR_ID')

    specs = import_module(venue_module_name, 'tournament.tournament_facts')
    schedule = ScheduleRepository.scrape_schedule_of_mitg_by_spec(
        getattr(specs, tournament_spec_name))

    if not CalendarPolicy.is_calendar_type_satisfied(calendar_type):
        raise ValueError(
            'Wrong calendar type %s. Available types are %s',
            calendar_type,
            CalendarPolicy.CALENDAR_TYPES)

    if calendar_type == 'google_calendar':
        credential, project = google.auth.default()
        getattr(CalendarService, f'register_{calendar_type}')(schedule, credential, calendar_id)
