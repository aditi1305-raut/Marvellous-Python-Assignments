'''
Write a Program which contains one function named as ChkNum() which accepts one parameter
as number . If number is even then it should display "Even Number"
 Otherwise display "Odd Number " On console .
 Input : 11    Output : Odd Number
 Input : 8     Output : Even Number
'''

def ChkNum():
    print("Enter a Number: ")
    num = int(input())

    if num /2 ==0:
        print("Even Number")

    else:
        print("Odd Number")

ChkNum()