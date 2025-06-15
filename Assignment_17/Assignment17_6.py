import time
import schedule

def LunchTime():
    print("It is Lunch Time !!")

def WrapUpWork():
    print("Wrap up Work..!!")


def main():

    schedule.every().day.at("13:23").do(LunchTime)

    schedule.every().day.at("13:25").do(WrapUpWork)

    while(True):

        schedule.run_pending()

        time.sleep(1)

if __name__ == "__main__":
    main()