import os
import sys

def main():

    print("Enter The File Name: ")
    filename = input()

    print("Enter the String: ")
    word = input()

    ret = os.path.exists(filename)

    if(ret == True):

        count = 0

        data = open(filename,'r')
        

        for line in data:
            words = line.split()

            for i in words:
             if (i == word):
               count = count + 1
        print("Frequency of String: ",count)

if __name__ == "__main__":
    main()