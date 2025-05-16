def Compare(A):
    if (A>=70 and A<=90): 
        return True
    
Increase = lambda A: (A + 10)

Product = lambda A,B : (A*B)
   
def FilterX(Task,Values):
    Result = []
    
    for no in Values:
        ret = (Task(no))
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
    Result = 1

    for no in Values:
        Result = Task(Result,no)

    return Result

def main():
    Data = []
    print("Enter The number of elements: ")
    Size = int(input())

    print("Please Enter the numeic Values: ")
    for i in range(Size):
        no = int(input())
        Data.append(no)
    
    print("Input Data : ",Data)




    FData = list(FilterX(Compare,Data))
    print("Filter Output is: ",FData)

    MData = list(MapX(Increase,FData))
    print("Output for Mapping: ",MData)

    RData = ReduceX(Product,MData)
    print("Output for the Reduce : ",RData)

if __name__ =="__main__":
    main()



