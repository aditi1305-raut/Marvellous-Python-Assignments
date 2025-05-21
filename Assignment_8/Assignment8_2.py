import threading

def EvenFactor(no):
    sum = 0
    for i in range(2,no+1):
        if (no%i==0 and i%2 == 0):
            sum = sum + i
    print("Sum of Even Factors: ",sum)

def OddFactor(no):
    sum = 0
    for i in range(1,no+1):
        if (no%i==0 and i%2!=0):
            sum = sum + i
    print("Sum of Odd factors: ",sum)

def main():

    print("Enter a Number: ")
    num = int(input())

    T1 = threading.Thread(target = EvenFactor(num))
    T1.start()

    T2 = threading.Thread(target = OddFactor(num))
    T2.start()

    T1.join()
    T2.join()



if __name__ == "__main__":
    main()