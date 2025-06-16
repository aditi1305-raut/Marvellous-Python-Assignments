import os
import sys


def main():

    print("Enter the file name: ")
    filename = input()

    ret = os.path.exists(filename)

    if (ret == True):

        firstfile = open(filename,'r')

        secondfile = open("Demo2.txt",'w')

        for lines in firstfile:

            
            secondfile.write(lines)

    else:
        print("file does not exists")

if __name__ == "__main__":
    main()