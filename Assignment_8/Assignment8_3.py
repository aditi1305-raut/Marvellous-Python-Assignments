import threading

def EvenList(nums):
    sum = 0
    for no in nums:
        if (no %2 == 0):
            sum = sum + no
    print("Sum of Even Elemenst: ",sum)


def OddList(nums):
    sum = 0
    for no in nums:
        if ( no%2 != 0):
            sum = sum + no
    print("Sum of Odd Elemenst: ",sum)



def main():
    data = []

    print("Enter The Number of Elements: ")
    Size = int(input())

    print("Enter the Numerical Values: ")
    for no in range(Size):
        no = int(input())
        data.append(no)

    T1 = threading.Thread(target = EvenList,args=(data,))
    T1.start()

    T2 = threading.Thread(target = OddList,args=(data,))
    T2.start()

    T1.join()
    T2.join()



if __name__ == "__main__":
    main()