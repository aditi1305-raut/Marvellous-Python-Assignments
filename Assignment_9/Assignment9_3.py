import os
import multiprocessing

def Factorial(nums):
    fact = 1
    for i in range(1,nums+1):
        fact = fact * i
    return fact

def main():
    data = [4,5,6,7,8]
    Result = []

    process1 = multiprocessing.Pool()
    Result = process1.map(Factorial,data)

    process1.close()
    process1.join()

    print(Result)

if __name__ == "__main__":
    main()