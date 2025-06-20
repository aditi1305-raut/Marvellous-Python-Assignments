'''
Design a Automation Script which accepts directory name and mail id from user and create log file 
in that directory which contains information  of running processes as its name ,PID , username . 
After Creating log file send that log file to the specified mail.

'''

import psutil
import schedule
import os
import hashlib
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import ssl


def ProcessInfo():

    print("Information of Currently Running Processes")

    ListProcess = []

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs = ['name','pid','username'])
        #print(info)

        ListProcess.append(info)

    return ListProcess


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


def SendingEmail(DirectoryName , Email_id):
    subject = "Text File sent using Python"
    body = "This is the body of the text message"
    sender_email = "aditi.raut.1305@gmail.com"
    sender_pass = "slghpxblmazrvhsw"
    receiver_email = Email_id
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465

    

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    body_part = MIMEText(body)
    #msg.attach(body_part)

    #Section 1 to attach file

    flag = os.path.isabs(DirectoryName)

    if (flag == False):

        flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("Path is Invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag == False):
        print("Path is valid but Directory not found..")
    for FolderName , SubFolderNames , FileNames in os.walk(DirectoryName):
        for FileNames in FolderName:
            file_path = os.path.join(DirectoryName,FileNames) 
            
            if os.path.isfile(file_path):
                LogFile = open(file_path , 'rb')
                Log_data = LogFile.read()


    #Attach file with filename to the email

    #msg.attach(MIMEApplication(f.read() ,Name = FileNames))
                msg.attch(MIMEApplication(Log_data , maintype = 'application',subtype='octect-stream',file_name = FileNames))

    #Section 2 for sending email
    server= smtplib.SMTP_SSL(smtp_server,smtp_port)

    server.login(sender_email , sender_pass)
    server.sendmail(sender_email,receiver_email,msg.as_bytes())

    print("Email sent Successfully")
    

def main():

    Arr = ProcessInfo()

    print("Enter The Name of Directory")
    Dir_name = input()
    
    Result = DirectoryWatcher(Dir_name,Arr)
    print(Result)
    

    print("Enter the Email id: ")
    Email_address = input()

    SendingEmail(Dir_name, Email_address)

    print("mail sent")
    

if __name__ == "__main__":
    main()

