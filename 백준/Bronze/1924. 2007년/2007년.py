import datetime

days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
x,y = map(int, input().split())
day = days[datetime.date(2007, x, y).weekday()]
print(day)