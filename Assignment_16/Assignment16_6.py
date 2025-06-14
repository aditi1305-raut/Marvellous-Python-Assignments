import os 
import sys


def main():

    filename = sys.argv[1]
    ret = os.path.exists(filename)


    if (ret == True):

        print("File Exists in current directory")
        with open('src.txt','r') as firstfile , open('dest.txt','w') as secondfile:

            #Read the contents from first file
            for lines in firstfile:
                secondfile.write(lines)

    else:
        print("File does not exists")


if __name__ =="__main__":
    main()