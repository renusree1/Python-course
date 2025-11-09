import random
import time
def random_date_time(start, end):
    print("Printing a random date and time between", start, "and", end)
    format= '%d/%m/%Y'
    start= time.mktime(time.strptime(start, format))
    end= time.mktime(time.strptime(end, format))
    random_time= start + random.random() * (end - start)
    ranodm_date= time.strftime(format, time.localtime(random_time))
    return ranodm_date
print("random date is:", random_date_time("1/12/2025", "31/12/2025"))