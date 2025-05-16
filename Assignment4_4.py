Evens = lambda Num : (Num%2==0)
Squares = lambda Num : (Num**2)
Sum = lambda A , B : (A + B)

def FilterX(Task , Values):
    Result = []

    for no in Values:
        ret = Task(no)
        if (ret==True):
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
    print("Enter the number of Elements: ")
    Size = int(input())

    print("Please Enter The Numeric Values: ")
    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data: ",Data)

    FData = list(FilterX(Evens,Data))
    print("Output for Filter: ",FData)

    MData = list(MapX(Squares,FData))
    print("Output of Map: ",MData)

    RData = ReduceX(Sum,MData)
    print("Output for Reduce: ",RData)

if __name__ =="__main__":
    main()