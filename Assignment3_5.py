from  MarvellousNum import ChkPrime

def List_Prime():
    Data = []
    print("Enter the Number of Elements: ")
    Size = int(input())

    print("Enter the Numeric Values: ")
    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data: ",Data)

    sum = 0
    
    for num in Data:
        if ChkPrime(num):
            sum = sum + num
    
    print("Addition of the Prime Number: ",sum)

List_Prime()