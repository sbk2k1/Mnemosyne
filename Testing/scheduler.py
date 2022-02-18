import schedule
import time
import datetime

def job():
    print(datetime.datetime.now())

schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()