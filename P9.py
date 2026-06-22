'''#math modules
import math
print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)
print(math.nan)

# basic functions
import math
print(math.sqrt(2))
print(math.pow(3,2))
print(math.fabs(3))
print(math.factorial(2))
print(math.gcd(3,4))
print(math.lcm(3,4))

# rounding function
import math
print(math.ceil(2.5))
print(math.floor(2.5))
print(math.trunc(2.5))
print(round(2.5))

#trigonometric functions
import math
print(math.sin(90))
print(math.cos(270))
print(math.tan(180))
print(math.asin(1))
print(math.acos(1))
print(math.atan(1))

#time
import time
print(time.time())
print(time.ctime())
print(time.localtime())
print(time.gmtime())
print(time.asctime())
time.sleep(2)
print(time.strftime("%d-%m-%Y"))
print(time.strftime("%H:%M:%S"))
print(time.mktime(time.localtime()))
print(time.perf_counter())

#calendar
import calendar
print(calendar.calendar(2026))
print(calendar.month(2026, 6))
print(calendar.monthrange(2026, 6))
print(calendar.isleap(2024))
print(calendar.leapdays(2000, 202))
print(calendar.weekday(2026, 6, 5))
print(calendar.month_name[6])
print(calendar.day_name[4])'''

#datetime
from datetime import datetime,date
print(datetime.now())
print(datetime.now().date())
print(datetime.now().time())
print(datetime.now().strftime("%d-%m-%YY"))
print(datetime.strptime("05-06-2026", "%d-%m-%Y"))
print(datetime.now() + datetime.timedelta(days=5))
print(datetime.now().timestamp())
print(datetime.now().weekday)
print(datetime.now().replace(year=2030))