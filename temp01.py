import datetime as dtt

monthday = dtt.datetime.now()
strdate = monthday.strftime('%m-%d')
# print(monthday.date().replace(year=1999))
print(strdate)