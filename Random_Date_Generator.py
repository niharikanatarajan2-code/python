import random
import time
def getRandomDate(start_date, end_date):
    print("Printing random date between", start_date, "and", end_date)
    randomGenerator = random.random()
    dateFormat="%m/%d/%Y"
    start_time = time.mktime(time.strptime(start_date, dateFormat))
    end_time = time.mktime(time.strptime(end_date, dateFormat))
    randomTime = start_time + randomGenerator * (end_time - start_time)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate
print("Random Date=", getRandomDate("1/1/2016", "12/12/2018"))