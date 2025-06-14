import os
import sys

def main():

    print("Enter the file name: ")
    filename = input()

    #print("Enter the data you want to write:")
    Students = ["Aditi","Jay","Sneha","Rutu","Avate"]
    
    fobj = open(filename,"w")
    for name in Students:
        fobj.write(name +"\n")

    
    fobj.close()

if __name__ == "__main__":
    main()