'''
Design a Automation Script which display information of running processes as its name , PID,username.
'''

import psutil

def ProcessInformation():

    Border = "-"*80

    print(Border)
    print("Information of Current running Processes")
    print(Border)


    for proc in psutil.process_iter():

        info = proc.as_dict(attrs=['pid' ,'name','username' ])
        print(info)


def main():

    ProcessInformation()


if __name__ == "__main__":
    main()