import datetime
import calendar
date=input()
WeekdayNumber = datetime.datetime.strptime(date, '%m %d %Y').weekday()
print(str(calendar.day_name[WeekdayNumber]).upper())