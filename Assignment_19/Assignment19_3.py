import os
import sys
import time
import shutil

def DirectoryWatcher(FirstDir , SecndDir):

    flag = os.path.isabs(FirstDir)

    if (flag == False):
        FirstDir = os.path.abspath(FirstDir)

    flag = os.path.exists(FirstDir)

    if(flag ==False):
        print("The Path is Invalid")
        return

    flag = os.path.isdir(FirstDir)

    if(flag==False):
        print("Path is valid but the destination is not Directory")
        exit()

    if not os.path.exists(SecndDir):
        os.mkdir(SecndDir)

    for FileName in os.listdir(str(FirstDir)):
        Source_file = os.path.join(FirstDir,FileName)
        destn_file = os.path.join(SecndDir , FileName)

        if (os.path.isfile(Source_file)):
            shutil.copy(Source_file , destn_file)

            print(f"Copied: {FileName}")


def main():

    #DirectoryWatcher("Demo" ,"Sample" )
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