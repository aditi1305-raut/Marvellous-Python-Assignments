import os
import sys

def main():

    print("Enter the file Name: ")
    filename = input()

    ret = os.path.exists(filename)

    if (ret == True):

        fobj = open(filename , 'r')

        data = fobj.read()

        print("Displaying the Contents: \n",data)


if __name__ == "__main__":
    main()