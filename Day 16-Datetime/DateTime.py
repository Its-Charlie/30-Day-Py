import datetime
from datetime import datetime, date, time, timedelta

#Current Date & Time
now = datetime.now()

now.day
now.month
now.year
now.hour
now.minute
now.second
now.timestamp()

#Create Date/Time
datetime(2025, 8, 2, 10, 30, 0)

date(2025, 8, 2)

time(10, 30, 50)

#Format Date (strftime)
now.strftime("%H:%M:%S")
now.strftime("%d/%m/%Y")
now.strftime("%m/%d/%Y, %H:%M:%S")

'''Common format codes:

%Y -> Year
%m -> Month
%d -> Day
%H -> Hour (24)
%M -> Minute
%S -> Second
%B -> Full month name
%A -> Weekday'''
