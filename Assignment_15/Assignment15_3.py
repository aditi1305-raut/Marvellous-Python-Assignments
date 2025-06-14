import os
import sys


def main():
    #print("Enter the file name: ",sys.argv[2])

    filename = sys.argv[1]
    ret = os.path.exists(filename)

    if (ret == True):
        print("File Exists in the Current Directory")

        with open('Demo.txt','r') as firstfile,open('ABC.txt',"w") as secondfile:

            #Read the contents from first file

            for lines in firstfile:

                #write content into second file
                secondfile.write(lines)
    
    else:
        print("File does not exist")



if __name__ == "__main__":
    main()