import os
import sys

def main():

    filename = "data.txt"

   # file = open(filename,"r")

    with open(filename,"r") as file:
            data = file.read()
                
            
            #num_words = len(words)

            for line in file :
                 words  = data.split()
                 if (len(words) >= 5):
                    print(line.strip())

    #file.close()           
                       

if __name__ == "__main__":
    main()