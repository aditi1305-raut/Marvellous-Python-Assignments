import os
import sys
import shutil
import time

def DirectoryWatcher(SourceDir , DestnDir , FileExt):

    flag = os.path.isabs(SourceDir)

    if (flag == False):
        SourceDir = os.path.abspath(SourceDir)

    flag = os.path.exists(SourceDir)

    if (flag == False):
        print("Path is Invalid")
        exit()

    flag = os.path.isdir(SourceDir)
    
    if (flag == False):
        print("Path is valid but target is not Directory")

    if not os.path.exists(DestnDir):
        os.mkdir(DestnDir)

    for FileName in os.listdir(str(SourceDir)):
        if FileName.endswith(FileExt):
            source_file = os.path.join(SourceDir , FileName)
            destn_file = os.path.join(DestnDir , FileName)


            shutil.copy(source_file , destn_file)

            print(f"Copied: {FileName}")


def main():

    #DirectoryWatcher("Demo" , "Sample2" ,".txt")
    Border = "-"*80
    print(Border)

    print("---------------------------------Marvellous Automations-------------------------------------------------------")

    print(Border)

    if(len(sys.argv)==4):
        if(sys.argv[1]== "--h") or (sys.argv[1]=="--H"):
            print("This Application is for used to Perform Sorting files wrt to Extensions")
            print("This is a Directory Automation Script")

        elif(sys.argv[1]=="--u") or (sys.argv[1]=="--U"):
            print("Use the given Script as")
            print("ScriptName.py NameOfDirectory")
            print("Please provide valid Absolute path")

        else :
            DirectoryWatcher(sys.argv[1],sys.argv[2],sys.argv[3])

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


