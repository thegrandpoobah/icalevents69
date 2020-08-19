from datetime import date, timezone
from icalevents.icalevents import events


evnts = events(file='./holidays.ics',
               start=date(2020, 9, 1), end=date(2020, 9, 30))
for event in evnts:
    print(event)
