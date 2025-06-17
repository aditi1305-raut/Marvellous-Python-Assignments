
import os
import sys
import time 
import schedule  

import hashlib              #used to calculate checksum

def CalculateChecksum(path,BlockSize=1024):
    fobj = open(path , 'rb')

    hobj = hashlib.md5() 

    buffer = fobj.read(BlockSize)   
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()

    return hobj.hexdigest()



def DirectoryWatcher(DirectoryName = "Marvellous"):
    
    flag = os.path.isabs(DirectoryName)

    if (flag==False):
        DirectoryName = os.path.abspath(DirectoryName)
        
    flag = os.path.exists(DirectoryName)

    if (flag == False):
        print("The Path is Invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if (flag == False):
        print("Path is invalid but the target is not a directory")
        exit()
    

    for FolderName , SubFolderNames , FileNames in os.walk(DirectoryName):
        
        for fname in  FileNames:
            fname = os.path.join(FolderName , fname )
            Checksum = CalculateChecksum(fname)
            print("File name: ",fname)
            print("Checksum: ",Checksum)
            print()
            
    timestamp = time.ctime()

    filename = "log.txt" 
    
    fobj = open(filename,"w")

    Border = "-"*54

    fobj.write(Border + "\n")
    fobj.write("This is a Log file of Marvellous Automation Script\n")
    fobj.write(Border+"\n")

   
    fobj.write("\n\n\n\n\n\n\n\n")
    fobj.write(Border+"\n")
    fobj.write("This File is created at \n"+timestamp+ "\n")

    fobj.write(Border+"\n")
    

    
def FindDuplicate(DirectoryName = "Marvellous"):
    
    flag = os.path.isabs(DirectoryName)

    if (flag==False):
        DirectoryName = os.path.abspath(DirectoryName)
        
    flag = os.path.exists(DirectoryName)

    if (flag == False):
        print("The Path is Invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if (flag == False):
        print("Path is valid but the target is not a directory")
        exit()
    

    Duplicate = {}

    for FolderName , SubFolderNames , FileNames in os.walk(DirectoryName):
        
        for fname in  FileNames:
            fname = os.path.join(FolderName , fname )
            Checksum = CalculateChecksum(fname)

            if Checksum in Duplicate:
                Duplicate[Checksum].append(fname)

            else:
                Duplicate[Checksum] = [fname]

    return Duplicate


def Displayresult(MyDict):
    Result = list(filter(lambda X : len(X)>1 , MyDict.values()))

    count = 0

    for value in Result:
        for subvalue in value:
            count = count + 1
            print(subvalue)
        print("-----------------------------------------------------------------")
        print("Value of Count is:  ",count)
        print("-----------------------------------------------------------------")
        count = 0


def DeleteDuplicate(Path="Marvellous"):

    MyDict=FindDuplicate(Path)
    Result = list(filter(lambda X : len(X)>1 , MyDict.values()))

    count = 0
    cnt = 0        #Total deleted values

    for value in Result:
        for subvalue in value:
            count = count + 1
            
            if(count > 1):
                print("Deleted File: ",subvalue)
                os.remove(subvalue)
                cnt = cnt + 1
        
        count = 0

    print("Total Deleted File: ",cnt)


         
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

 
        else:
           Result =DeleteDuplicate(sys.argv[1])
           print(Result)
    
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