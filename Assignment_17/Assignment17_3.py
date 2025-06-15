import schedule
import time
import datetime

def MySchedule():
    print("Do Coding..!")

def main():

    print("Do Coding..!")

    schedule.every(30).minutes.do(MySchedule)

    while(True):

        schedule.run_pending()

        time.sleep(1)

if __name__ == "__main__":
    main()