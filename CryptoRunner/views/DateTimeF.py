# from datetime import datetime,timezone,timedelta
# дублирования функсий из datetime (без етого не роботае в некоторих местах)
import datetime


def datetime_now_F():
    return datetime.datetime.now(datetime.timezone.utc)

def timezone_utc():
    return datetime.timezone.utc

def timedelta_F(days=0,seconds=0,microseconds=0,milliseconds=0,minutes=0,hours=0,weeks=0):
    return datetime.timedelta(days=days,seconds=seconds,microseconds=microseconds,
                     milliseconds=milliseconds,minutes=minutes,hours=hours,weeks=weeks)


def datetime_today():
    datetime.datetime.today()






