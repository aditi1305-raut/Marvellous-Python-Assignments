from functools import reduce

Compare = lambda nums : (nums >= 70 and nums<= 90)

Increment = lambda nums: (nums + 10)

Product = lambda A ,B : (A * B)

def main():
    Data = []

    print("Enter the Number of Elements: ")
    Size = int(input())

    print("Enter the numeric Values: ")
    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data: ",Data)

    FData = list(filter(Compare,Data))
    print("List After Filter: ",FData)

    MData = list(map(Increment,FData))
    print("List After Map: ",MData)

    RData = reduce(Product,MData)
    print("Output for Reduce: ",RData)



if __name__ =="__main__":
    main()