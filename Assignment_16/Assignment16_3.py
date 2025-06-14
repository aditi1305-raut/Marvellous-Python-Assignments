import os
import sys

def main():

    print("Enter the file name: ")
    filename = input()

    line_count = 0
    word_list = 0
    char_count = 0
    ret = os.path.exists(filename)
    
    if (ret == True):

        #file = open(filename,"r")
        #data = file.read()

        with open(filename,"r") as file:
            data = file.read()

            with open(filename,"r") as file:
                for line in file:
                    line_count =line_count + 1
            
                print("Total Lines: ",line_count)

            file.close()

            #Word count
            word_list = data.split()
            num_words = len(word_list)

            print("Number of Words: ",num_words)

            #character Count
            for char in data:
                    char_count = char_count + 1
            print("Number of characters in data: ",char_count)
                   

if __name__ == "__main__":
    main()