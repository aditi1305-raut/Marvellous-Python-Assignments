'''
Design a Automation Script which accept directory name from user and create a log file in that 
directory which contains information of running processses as its name , PID , username.

'''

import psutil
import os
import time

def ProcessInformation():

    listProcess = []

    Border = "-"*80
    print(Border)

    print("Information of Currently Running Processes: ")

    for proc in psutil.process_iter():

        info = proc.as_dict(attrs = ['pid','name','username'])
        print(info)

        listProcess.append(info)

    return listProcess

def DirectoryWatcher(DirectoryName , Data):

    
    if not os.path.exists(DirectoryName):

        os.mkdir(DirectoryName)

    timestamp = time.ctime()

    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("/","_")

    filename = os.path.join(DirectoryName, "Marvellous%s.log"%(timestamp))

    fobj = open(filename ,"w")

    Border = "-"*80
    fobj.write(Border)
    fobj.write("\n\t\tMarvellous Infosystems Process Log\n")
    fobj.write(f"\n\t\t File is Created at  "+time.ctime()+"\n")

    for value in Data:
        fobj.write("%s \n\n" %value)

    fobj.write(Border)

    fobj.close()

def main():

    Arr = ProcessInformation()

    Result = DirectoryWatcher("Sample" , Arr)

    print(Result)

if __name__ == "__main__":
    main()
