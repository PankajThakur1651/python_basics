import datetime
import pytz

todays_date = datetime.date.today()
print(todays_date)

birth_date = datetime.date(2024, 9,5)

print(f"birth date is ${birth_date}")

days_left = birth_date-todays_date
print (f"days left for birthday {days_left}")

# time left
time_now = datetime.time(1,2,3)
print (f"now time is {time_now}")

#datetime.datetime
dt = datetime.datetime(2024, 5,6)
print(dt)

for tz in pytz.all_timezones:
    print(f"time zone is {tz}")