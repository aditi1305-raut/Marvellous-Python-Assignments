import os
import sys
import time
import hashlib

def CalculateChecksum(Path):

    fobj = open(Path , 'rb')

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)
    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest() 

def DirectoryWatcher(DirectoryName):

    flag = os.path.isabs(DirectoryName)

    if (flag == False):

        flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("Path is Invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag == False):
        print("Path is valid but Directory not found..")

    for FolderName , SubFolderName , FileName in os.walk(DirectoryName):

        for fname in FileName:
            fname = os.path.join(FolderName,fname)

            checksum = CalculateChecksum(fname)
            print("File Name is: ",fname)
            print("Checksum is: ",checksum)

            print()

    timestamp = time.ctime()

    filename = "MarvellousLog%s.log" %(timestamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")

    Data = open(filename,"w")

    Border = "-"*54

    Data.write(Border + "\n")
    Data.write("This is a Log file of Marvellous Automation Script\n")
    Data.write(Border+"\n")

   
    Data.write("\n\n\n\n\n\n\n\n")
    Data.write(Border+"\n")
    Data.write("This File is created at \n"+timestamp+ "\n")

    Data.write(Border+"\n")


    
def FindDuplicate(DirectoryName):
        
    flag = os.path.isabs(DirectoryName)

    if (flag == False):
         DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
            print("Path is Invalid")
            return

    flag = os.path.isdir(DirectoryName)

    if(flag == False):
            print("Path is valid but Directory not found..")
            exit()

    Duplicate = {}

    for FolderName , SubFolderNames , FileNames in os.walk(DirectoryName):

    #for FileNames in os.listdir(DirectoryName):
        for fname in FileNames :
                fname = os.path.join(FolderName , fname)
                checksum = CalculateChecksum(fname)

                if checksum in Duplicate:
                    Duplicate[checksum].append(fname)
                    

                else:
                    Duplicate[checksum] = [fname]

        return Duplicate


def main():

    Border = "-"*80
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
           Result = FindDuplicate(sys.argv[1])
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




    '''Result = FindDuplicate("Demo")
    print(Result)
'''
if __name__ == "__main__":
    main()