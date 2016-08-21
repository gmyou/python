# date
from datetime import date
d = date.today()
print d
print d.isoformat()
print d.ctime()
print d.strftime("%y/%m/%d")
print d.strftime("%Y-%m-%d")

# local time
from time import localtime, strftime
print strftime("%Y-%m-%d %H:%M:%S")
print strftime("%Y-%m-%d %H:%M:%S", localtime())

# datediff
d0 = date(2008, 8, 18)
d1 = date(2008, 9, 26)
delta = d0 - d1
print delta.days

from datetime import datetime
date_format = "%m/%d/%Y"
a = datetime.strptime('8/18/2008', date_format)
b = datetime.strptime('9/27/2008', date_format)
delta = b - a
print delta.days

a = datetime.strptime('2016-08-19 13:49', date_format)
b = datetime.strptime('2016-08-21 10:49', date_format)
delta = b - a
print delta

#timedelta
print "############ timedelta #############"
from datetime import timedelta
now = datetime.now()
dday = now + timedelta(days=1) + timedelta(hours=20)
print now.ctime(), ' 1day 20hours increament day is ', dday.ctime()
