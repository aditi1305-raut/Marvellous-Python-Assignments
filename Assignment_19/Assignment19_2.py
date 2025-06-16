
import os
import time
import sys

def DirectoryWatcher(DirectoryName , old_ext , new_ext):
     
    
    if not os.path.isdir(DirectoryName):
        print(f"Directory '{DirectoryName}' does not exist")
        return

    #for FolderName , SubFolderName , FileName in os.walk(str(DirectoryName)):
    for FileName in os.listdir(str(DirectoryName)):
        #for FileName in FolderName:
            if FileName.endswith(old_ext):
                
                
                old_file = os.path.join(DirectoryName,FileName)
                
                Changed_name = FileName.replace(old_ext , new_ext)
                new_file = os.path.join(DirectoryName, Changed_name )

                os.rename(old_file,new_file)

            

            print(f"Renamed '{FileName}' -> {FileName.replace(old_ext,new_ext)}")
            

def main():

     #DirectoryWatcher("Demo",".txt",".doc")

    Border = "-"*80
    print(Border)

    print("---------------------------------Marvellous Automations-------------------------------------------------------")

    print(Border)

    if(len(sys.argv)==4):
        #DirectoryWatcher(sys.argv[1],sys.argv[2],sys.argv[3])

        if(sys.argv[1]== "--h") or (sys.argv[1]=="--H"):
            print("This Application is for used to Perform Sorting files wrt to Extensions")
            print("This is a Directory Automation Script")

        elif(sys.argv[1]=="--u") or (sys.argv[1]=="--U"):
            print("Use the given Script as")
            print("ScriptName.py NameOfDirectory")
            print("Please provide valid Absolute path")

        else: 
            DirectoryWatcher(sys.argv[1],sys.argv[2],sys.argv[3])


    #elif(len(sys.argv)==2):
     #       DirectoryWatcher(sys.argv[1],sys.argv[2],sys.argv[3])

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








