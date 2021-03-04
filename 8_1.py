class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def int_date(cls, date):
        new_date = list(map(int, date.split('-')))
        return new_date, cls.valid_date(new_date)

    @staticmethod
    def valid_date(date):
        day, month, year = date
        if day > 31:
            return 'Invalid date'
        elif month > 12:
            return 'Invalid date'
        elif day > 29 and month == 2:
            return 'Invalid date'
        elif day == 29 and month == 2:
            return 'Valid date. This is leap year'
        else:
            return 'Valid date'


d_1 = Date
print(d_1.int_date('30-12-1999'))

