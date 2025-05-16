def Prime(Num):
    if Num == 1:
        return False
    
    for i in range(2,Num):
        if (Num%i==0):
            return False

    return True

def Multiply(Num):
    return Num*2 

def Max(Num1,Num2):
    return max(Num1,Num2)

def FilterX(Task,Values):
    Result = []

    for no in Values:
        ret = Task(no)
        if (ret == True):
            Result.append(no)
    
    return Result

def MapX(Task,Values):
    Result = []

    for no in Values:
        ret = Task(no)
        Result.append(ret)

    return Result

def ReduceX(Task,Values):
    Result = 0

    for no in Values:
        Result = Task(Result,no)

    return Result  

def main():
    Data = []
    print("Enter the Number of Elements: ")
    Size = int(input())

    print("Enter The Numeric Values: ")
    for i in range(Size):
        no = int(input())
        Data.append(no)
    
    print("Input Data: ",Data)

    FData = list(FilterX(Prime,Data))
    print("List After Filter: ",FData)

    MData = list(MapX(Multiply,FData))
    print("List After Map: ",MData)

    RData = ReduceX(Max,MData)
    print("Output of Reduce: ",RData)

if __name__ == "__main__":
    main()



