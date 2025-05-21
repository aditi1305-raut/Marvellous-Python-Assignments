from functools import reduce

Evens = lambda nums : (nums%2==0)

Squares = lambda nums: (nums**2)

Sum = lambda A ,B : (A + B)

def main():
    Data = []

    print("Enter the Number of Elements: ")
    Size = int(input())

    print("Enter the numeric Values: ")
    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data: ",Data)

    FData = list(filter(Evens,Data))
    print("List After Filter: ",FData)

    MData = list(map(Squares,FData))
    print("List After Map: ",MData)

    RData = reduce(Sum,MData)
    print("Output for Reduce: ",RData)



if __name__ =="__main__":
    main()