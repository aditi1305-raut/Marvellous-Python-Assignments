import os
import hashlib
import sys

def CalculateChecksum(Path):

    fobj = open(Path ,'rb')

    hobj = hashlib.md5()

    buffer = fobj.read(1024)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

    
    
def DirectoryWatcher(DirectoryName):    
    
    flag = os.path.isabs(DirectoryName)

    if (flag== False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("Path is Invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag == False):
        print("Path is valid but Directory not found..")


    for FolderName,SubFolderName , FileName in os.walk(DirectoryName):

        for fname in FileName:
            fname = os.path.join(FolderName , fname)
            checksum = CalculateChecksum(fname)
            print("File Name: ",fname)
            print("Checksum : ",checksum)
            print()

        
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
           DirectoryWatcher(sys.argv[1])

    else:
        print("Invalid number of Command Line Arguments")
        print("Use the given flags : " )
        print("--h: Used to Display the Help")
        print("--u: Used To display the Usage ")

    print(Border)
    print("------------------------- Thanks For Using our Script --------------------------")
    print("--------------------------Marvellous Infosystems ---------------------------------")
    print(Border)

    #DirectoryWatcher("Demo")
      

if __name__ == "__main__":
    main()