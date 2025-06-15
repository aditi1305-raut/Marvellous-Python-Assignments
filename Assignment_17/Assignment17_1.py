import schedule
import time
import sys
import datetime 


def myschedule():
    print("Jay Ganesh...!!!")

def main():

    print("Inside Automation")

    schedule.every(2).seconds.do(myschedule)

    while(True):
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    main()