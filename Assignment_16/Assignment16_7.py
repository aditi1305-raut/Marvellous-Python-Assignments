import os
import sys

def main():

    file = open("marks.txt","w")
    for i in range(5):
        print("Enter the name: ")
        name = input()

        print("Enter the marks: ")
        marks = int(input())

        file.write(f"{name} :{marks}")

    file.close()

    file = open("marks.txt" ,"r")
    print("Students Scoring more than 75: ")

    for line in file:
        name , marks = line.strip().split()

        if int(marks) > 75:
            print(f"{name} : {marks}")


if __name__ == "__main__":
    main()