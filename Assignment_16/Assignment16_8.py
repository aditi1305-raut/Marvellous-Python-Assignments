import os 
import sys

def main():

    with open("src.txt","r") as rawfile , open("cleaned.txt","w") as cleanfile:
        for line in rawfile:
            if line.strip():  #skip blank lines

                cleanfile.write(line)

        



if __name__ == "__main__":
    main()