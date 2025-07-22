'''
Problem Statement – Automation Script: Duplicate File Removal

Design a Python automation script that:

1. Accepts a directory name from the user.

2. Scans the directory and deletes all duplicate files by comparing their checksums.

3. Creates a folder named Marvellous, and inside it, generate a log file that:

Records the names of deleted duplicate files.

Contains the date and time when each duplicate file was deleted.

4. Accepts a time interval in minutes, and repeats the duplicate file removal task after that duration.

5. Accepts a mail ID from the user and sends an email with the log file attached.

-The email body should include:

-Starting time of the scan

-Total number of files scanned

-Total number of duplicate files found

'''


import os
import sys
import time 
import schedule  
from datetime import datetime
import hashlib              #used to calculate checksum
import smtplib
from email.message import EmailMessage
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import ssl


def CalculateChecksum(path,BlockSize=1024):
    fobj = open(path , 'rb')

    hobj = hashlib.md5() 

    buffer = fobj.read(BlockSize)   
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()

    return hobj.hexdigest()


      
def DirectoryDuplicate(FileName):

    StartTime = datetime.now()
    StartEpoch = time.time()
    
    if not os.path.isabs(FileName):
        FileName = os.path.abspath(FileName)
        
    if not os.path.exists(FileName):
        exit()

    if not  os.path.isdir(FileName):
        exit()
    
    TargetDir = "Marvellous"
    if not os.path.exists(TargetDir):
        os.mkdir(TargetDir)

    TimeStamp = StartTime.strftime("%Y-%m-%d_%H_%M_%S")
    Logpath = os.path.join(TargetDir, f"DuplicateDeleteLog_{TimeStamp} .log")

    fobj = open(Logpath , "w")

    Border = "-"*90

    fobj.write(Border)
    fobj.write("Deleted Duplicate Files log Details \n")
    fobj.write(("Date:" +StartTime.strftime("%Y-%m-%d") +"   Time: "+StartTime.strftime("%H:%M:%S")).center(90)+"\n" )
    
    fobj.write(Border + "\n")

    Duplicates = {}
    TotalFiles = 0
    DeletedFiles = 0
    DeletedDetails = []

    for Folder , Subfolders , Files in os.walk(FileName):
        for file in Files:
            Fname = os.path.join(Folder , file)

        if (os.path.abspath(Fname) == os.path.abspath(Logpath)):
            continue

        TotalFiles += 1
        checksum = CalculateChecksum(Fname)

        if checksum in Duplicates :
            os.remove(Fname)
            DeletedFiles += 1
            DeletedDetails.append(f"Deleted File: {os.path.basename(Fname)} \n Checksum : {checksum} \n\n")

        else:
            Duplicates[checksum] = Fname


    fobj.write(f"Scanning Started at : {StartTime} \n")
    fobj.write(f"Total Files Scanned : {TotalFiles} \n")
    fobj.write(f"Total Duplicates Found: {DeletedFiles} \n\n")

    fobj.write("Deleted Duplicate Files: \n\n")
    for entry in DeletedDetails:
        fobj.write(entry)

    EndTime = time.time()

    ExecutionTime = EndTime - StartEpoch
    fobj.write(f"Execution Time: {ExecutionTime} Seconds \n"  )
    fobj.write(Border +"\n")

    fobj.close()


    return Logpath , StartTime , TotalFiles , DeletedFiles 

def TimeInterval(Min, Directory , EmailSend):

    def Task():
        logfile , start , total ,deleted  = DirectoryDuplicate(Directory)
        SendMail(logfile , EmailSend , start , total , deleted)

    schedule.every(Min).seconds.do(Task)
    while(True):

        schedule .run_pending()
        time.sleep(1)

def SendMail(Logpath, receiver , StartTime , TotalFiles , DeletedFiles):
    Subject = "Duplicate File Removal Report"
    Body = (f"Report for Duplicate File Removal \nScanning Started at: {StartTime} \nTotal Files Scanned: {TotalFiles} \n Total Duplicate Files Found: {DeletedFiles}")

    sender = "aditi.raut.1305@gmail.com"
    password = "ehikekijnigvxoiq"

    fobj = open(Logpath , 'rb')
    log_data = fobj.read()
    fobj.close()

    msg = EmailMessage()
    msg['Subject'] = Subject
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content(Body)

    msg.add_attachment(
        log_data ,
        maintype = 'application',
        subtype='octet-stream',
        filename = os.path.basename(Logpath)
    )

    smtp = smtplib.SMTP_SSL('smtp.gmail.com' , 465)
    smtp.login(sender , password)
    smtp.send_message(msg)
    smtp.quit()



       
def main():
    
    Border = "-"*54
    print(Border)
   
    print("----------------------------- Marvellous Automations -----------------------------")
    print(Border)

    
    if (len(sys.argv)==2):
        if(sys.argv[1]=="--h") or (sys.argv[1]=="--H"):
            print("This Application is used to perform Directory Cleaning")
            print("This is the Directory automation Script")

        elif (sys.argv[1]=="--u") or (sys.argv[1]=="--U"):
            print("Use the Given Script as ")
            print("ScriptName.py NameOfDirectory")
            print("please provide valid absolute Path")

 
    elif (len(sys.argv)==4):
           Directory = sys.argv[1]
           TimeInt = int(sys.argv[2])
           EmailSend = sys.argv[3]
           print("Code Run Successfully")
           print(f"Directory name is: {Directory}\nTime Interval is: {TimeInt}\nEmail will be sent to:{EmailSend} ")

           print(Border + "\n")           
           
           TimeInterval(TimeInt , Directory ,EmailSend)
    
    else:
        print("Invalid number of Command Line Arguments")
        print("Use the given flags : " )
        print("--h: Used to Display the Help")
        print("--u: Used To display the Usage ")

    
    print(Border)
    print("------------------------- Thanks For Using our Script --------------------------")
    print("--------------------------Marvellous Infosystems ---------------------------------")
    print(Border)

    
    
if __name__ =="__main__":
    main()
