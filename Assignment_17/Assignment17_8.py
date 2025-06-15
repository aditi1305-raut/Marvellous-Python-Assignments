
import schedule
import time

def EmailCheck():
    print("Checking Emails..!!")


def main():

    print("Checking Emails..!!")

    schedule.every(10).seconds.do(EmailCheck)

    while(True):

        schedule.run_pending()

        time.sleep(1)


if __name__ == "__main__":
    main()