
import time
import datetime

def dt():
    begin = datetime.date(2000,1, 1)
    end = datetime.date(2020, 1, 1)

    unixdates=[]
    next_day = begin
    while True:
        if next_day > end:
            break;
        next_day += datetime.timedelta(days=1)
#        print(next_day)
	#unixtime= time.mktime(next_day.timetuple())
        #unixdates.append(int(unixtime))

    return next_day;
x = dt
print(x)

