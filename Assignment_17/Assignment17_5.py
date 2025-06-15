import schedule
import time
import datetime
import sys

def MySchedule():
    print("Current Time: ",datetime.datetime.now())

#def CreateLog():
    #timestamp = time.ctime()
    time_now = datetime.datetime.now()
    fobj = open("Marvellous.txt","a")
    fobj.write(str(time_now)+"\n")

def main():

    ntime = datetime.datetime.now()

    fobj = open("Marvellous.txt","a")
    fobj.write(str(ntime)+"\n")

    schedule.every(1).minute.do(MySchedule)

    while(True):
        schedule.run_pending()

        time.sleep(1)

if __name__ == "__main__":
    main()




