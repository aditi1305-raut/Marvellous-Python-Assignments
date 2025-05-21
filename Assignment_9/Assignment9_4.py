import os
import threading
import multiprocessing
import time

def Sum(start,end):
    sum = 0
    for i in range(1,end+1):
        sum = sum + i
    return sum

def Sum_Thread(nums):
    sum = 0
    for i in range(1,nums):
        sum = sum + i
    return sum

def Sum_Mutiprocess(nums):
    sum = 0
    for i in range(1,nums):
        sum = sum + i
    return sum


def main():

    #Normal Function
    num_range =10000000
    start_time = time.time()
    Addition = Sum(1,num_range)
    print("Addition is ",Addition)
    end_time = time.time()

    print("Total Execution time using Normal Function: ",(end_time-start_time))

    #Threading
    start_time = time.time()
    thread1 = threading.Thread(target=Sum_Thread,args=(num_range,))
    thread1.start()
    thread1.join()
    end_time = time.time()

    print("Total Execution time using Threading : ",(end_time-start_time))

    #Multiprocessing
    start_time = time.time()
    process = multiprocessing.Pool()
    Result = process.map(Sum_Mutiprocess,num_range)

    process.close()

    process.join()
    print(Result)

    end_time= time.time()

    print("Total Execution time using Multiprocessing : ",(end_time-start_time))


if __name__ == "__main__":
    main()



