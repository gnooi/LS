"""

- define a class MeetUp
    - define an init method to accept year, month
        - initialize self.year to year
        - initialize self.month to month

    - define an instance method day to accept 1 day, 1 descriptor
        - determine the exact date of the day in that year based on the descriptor
        - determine the first day of that month for that year 
        - then calculate based on the descriptor the day 
        - return year, month, day as a date object


- first: 1 - 7
- second: 8 - 14
- third: 15 - 21
- fourth: 22 - 28
- fifth: 29 - 31 
- teenth: 13, 14, 15, 16, 17, 18, 19
"""
import datetime

class Meetup:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def day(self, day, descriptor):
        # Normalize input for consistency
        day = day.capitalize()
        descriptor = descriptor.lower()

        # Descriptor ranges
        descriptors = {
            'first': range(1, 8),
            'second': range(8, 15),
            'third': range(15, 22),
            'fourth': range(22, 29),
            'fifth': range(29, 32),
            'teenth': range(13, 20),
        }

        if descriptor == 'last':
            return self._get_last_day(day)

        date_range = descriptors.get(descriptor)
        if date_range is None:
            raise ValueError(f"Invalid descriptor: {descriptor}")

        for date in date_range:
            if self._matches_day(day, date):
                return datetime.date(self.year, self.month, date)

        return None

    def _get_last_day(self, day):
        last_day = self._calculate_last_day_of_month()
        for date in range(last_day, 0, -1):
            if self._matches_day(day, date):
                return datetime.date(self.year, self.month, date)

    def _calculate_last_day_of_month(self):
        # Find the first day of the next month
        if self.month == 12:
            next_month = datetime.date(self.year + 1, 1, 1)  # January of the next year
        else:
            next_month = datetime.date(self.year, self.month + 1, 1)  # First day of the next month

        # Subtract 1 day to get the last day of the current month
        last_day = next_month - datetime.timedelta(days=1)
        return last_day.day

    def _matches_day(self, day, date):
        try:
            current_date = datetime.date(self.year, self.month, date)
            return current_date.strftime("%A") == day
        except ValueError:
            return False
