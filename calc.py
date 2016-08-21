# date
import datetime
d = datetime.date.today()
print d
print d.isoformat()
print d.ctime()
print d.strftime("%y/%m/%d")
print d.strftime("%Y-%m-%d")

# local time
from time import localtime, strftime
print strftime("%Y-%m-%d %H:%M:%S")
print strftime("%Y-%m-%d %H:%M:%S", localtime())

# calc
# print d+2
