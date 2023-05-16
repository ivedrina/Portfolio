
import schedule
import time

def task():
    list=[1,5,6,7]
    result= ''
    for i in list:
        result += str(i)
    print(result)

schedule.every(2).seconds.do(task)

while True:
    schedule.run_pending()
    #time.sleep(1)