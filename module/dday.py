from datetime import datetime, timedelta

def dday(day, hour):
    now = datetime.now()
    dday = now + timedelta(days=day) + timedelta(hours=hour)
    print now.ctime(), ' 1day 20hours increament day is ', dday.ctime()

# dday(1, 10)
