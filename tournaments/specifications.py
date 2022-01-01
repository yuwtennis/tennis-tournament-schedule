

class CalendarSpecification:

    CALENDAR_TYPES = ['google_calendar']

    @classmethod
    def is_calendar_type_satisfied(cls, calendar_type):

        if calendar_type not in cls.CALENDAR_TYPES:
            return False

        return True
