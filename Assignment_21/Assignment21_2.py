'''
Design a Automation Script which accept process name and display information of that process if 
it is running.

'''

import psutil

def ProcessInformation(ProcessName):

    Border = "-"*80
    print(Border)
    print("Information of Process: ")
    print(Border)

    for proc in psutil.process_iter():
        proc.info = proc.as_dict(attrs=['pid' ,'name','username' ])
        if proc.info['name'] == ProcessName:
            print("Process Name: ",proc.info['name'])
            print("Process ID: ",proc.info['pid'])
            print("User Name: ",proc.info['username'])

    return 
    

def main():

   Result  =ProcessInformation('Notepad.exe')
   


if __name__ == "__main__":
    main()