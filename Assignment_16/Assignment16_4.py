import sys
import os

def main():

    data = []
    
    for num in range(10):
        no = int(input())
        data.append(no)

   # print("Input Data : ",data) 
    
    #print("Enter the file name: ")
    filename = "numbers.txt"

    with open(filename, "w") as file:
        for num in data:
            file.write(str(num) + "\n")
    
    file.close()


if __name__ == "__main__":
    main()