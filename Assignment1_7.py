'''
Write a program which contains one function that accepts one number from user
and returns true if number is divisible by 5 otherwise return false.
'''

def CheckNum():
    print("Enter a Number: ")
    num = int(input())

    if num%5 == 0:
        print("True")

    else:
        print("False")

CheckNum()