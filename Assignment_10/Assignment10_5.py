from functools import reduce

def Prime(num):
        if num == 1:
            return False
        for i in range(2,num):
            if (num%i == 0):
                return False 
        return True 

Product = lambda nums: (nums*2)

Max = lambda num1,num2 : (max(num1,num2))

def main():
    Data = []

    print("Enter the Number of Elements: ")
    Size = int(input())

    print("Enter the numeric Values: ")
    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data: ",Data)

    FData = list(filter(Prime,Data))
    print("List After Filter: ",FData)

    MData = list(map(Product,FData))
    print("List After Map: ",MData)

    RData = reduce(Max,MData)
    print("Output for Reduce: ",RData)



if __name__ =="__main__":
    main()