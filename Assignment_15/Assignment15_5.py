import os
import sys

def main():

    filename = sys.argv[1]
    word = sys.argv[2]

    count = 0 
    file = open(filename,"r") 
       
    for line in file:
            words = line.split()
            for i in words:
                if (i == word):
                    count = count +1 
    print("Frequency of word in the file: ",count)


if __name__ == "__main__":
    main()