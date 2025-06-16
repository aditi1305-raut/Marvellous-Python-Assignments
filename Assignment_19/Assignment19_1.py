import os
import time
import sys

def DirectoryWatcher(DirectoryName,Extension):

    flag = os.path.isabs(DirectoryName)

    if (flag==False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)


    if(flag==False):
        print("The Path is Invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag==False):
        print("Path is valid but the target is not a directory")
        exit()

    for FolderName , SubFolderName , FileName in os.walk(DirectoryName):
        for fname in FileName:
        #fname = os.path.join(FolderName,fname)
            if(fname.endswith(Extension)):
                print(fname)


def main():

    #DirectoryWatcher("Demo" ,".py")

    
    Border = "-"*80
    print(Border)

    print("---------------------------------Marvellous Automations-------------------------------------------------------")

    print(Border)

    if(len(sys.argv)==2):
        if(sys.argv[1]== "--h") or (sys.argv[1]=="--H"):
            print("This Application is for used to Perform Sorting files wrt to Extensions")
            print("This is a Directory Automation Script")

        elif(sys.argv[1]=="--u") or (sys.argv[1]=="--U"):
            print("Use the given Script as")
            print("ScriptName.py NameOfDirectory")
            print("Please provide valid Absolute path")

    elif (len(sys.argv)==3):
            DirectoryWatcher(sys.argv[1],sys.argv[2])

    else:
        print("Invalid Number of Commandline Arguments")
        print("Use the given flags : ")
        print("--h : Used to display the Help ")
        print("--u: Used to Display Usage")


    print(Border)
    print("------------------------------Thank You for Using our Script---------------------------------------------- ")
    print("---------------------------------Marvellous Infosystems-------------------------------------------------------")


if __name__ == "__main__":
    main()