import sys
import os


def main():   #Assign the two parameters during commandline

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    content1 = open(file1 , 'r')
    data1 = content1.read()

    content2 = open(file2,'r')
    data2 = content2.read()

    if(data1 == data2):
        print("Success")

    else:
        print("Failure")

if __name__ == "__main__":
    main()