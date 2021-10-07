from datetime import date, timedelta


class Student:
    """ A Student class as a basee for method testing """
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        # start date set to date the instance is created
        self._start_date = date.today()
        # end date is one year from date instance created
        # but doesn't allow for leap year
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    def alert_santa(self):
        self.naughty_list = True

    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"
