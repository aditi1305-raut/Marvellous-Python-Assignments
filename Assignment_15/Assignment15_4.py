import os 
import sys

def main():

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    content1 = open(file1,"r")
    data1 = content1.read()

    content2 = open(file2,"r")
    data2 = content2.read()

    if (data1 == data2):
        print("Contents in both files are same")

    else:
        print("Contents in both files are different")

if __name__ =="__main__":
    main()