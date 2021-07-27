from calendar import Calendar
from datetime import date

DAYS = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4,
        'Saturday': 5, 'Sunday': 6}

def meetup(year, month, week, day_of_week):
    # days: list of dates in 3-tuple form (y, m, d) corresponding to
    # the specified day_of_week in that particular year
    cal = Calendar()
    days = [item[:3] for item in cal.itermonthdays4(year, month) 
            if item[1] == month and item[3] == DAYS[day_of_week]]
    
    if len(week) == 3:  # catch ordinal dates '1st', '3rd' etc
        pos = int(week[0]) - 1
        if pos >= len(days):
            raise MeetupDayException(f'{year}-{month} does not have {pos} weeks.')
        return date(*days[pos])
    elif week == 'last':
        return date(*days[-1])
    elif week == 'teenth':
        for day in days:
            if day[2] in range(13,20):
                return date(*day)
    else:
        raise Exception(f'Invalid week: {week}')


class MeetupDayException(Exception):
    # ???
    pass
