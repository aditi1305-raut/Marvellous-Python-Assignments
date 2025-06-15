import schedule
import time
import shutil
import datetime

def FileBackUp():

    source = "data.txt"
    destn = "Backup_log.txt"

    shutil.copy(source,destn)

    log = open("Backup_log.txt",'a')

    log.write(f"Backup done at : {datetime.datetime.now()}\n")
    print("Backup Completed")


def main():

    schedule.every(1).minute.do(FileBackUp)

    while(True):

        schedule.run_pending()

        time.sleep(1)

if __name__ == "__main__":
    main()
