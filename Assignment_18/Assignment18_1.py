import os
import sys

def main():

    print("Enter the file name")
    filename = input()

    ret = os.path.exists(filename)

    if(ret == True):
        print("The File is Exists in the Current Directory!!")

    else:
        print("file is not exists in Current Directory")


if __name__ == "__main__":
    main()