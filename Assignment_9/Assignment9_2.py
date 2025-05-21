import multiprocessing
import os

def SquareNums(nums):
    square = 1
    for i in range(nums):
        square = (nums * nums)
    return square
   


def main():
    data = [10,20,30,40,50]
    result = []

    process1 = multiprocessing.Pool()
    result = process1.map(SquareNums,data)

    process1.close()
    process1.join()

    print(result)




if __name__ =="__main__":
    main()