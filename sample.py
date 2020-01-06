import time
import datetime

def tb():
    begin = datetime.date(2005,2,2)
    end = datetime.date(2007,10,1)

    unixdates=[]
    next_day = begin
    while True:
        if next_day > end:
            break;
        next_day += datetime.timedelta(days=1)
        unixtime= time.mktime(next_day.timetuple())
        unixdates.append(int(unixtime))

    return unixdates;

#print(tb())
#print(len(tb()))
#2001-01-17
