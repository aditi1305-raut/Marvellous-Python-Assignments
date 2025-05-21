import threading
import time

def SerialNum(Nums):
    print("Numbers from 1 to 50 in serial order")
    for i in range(1,51):
        print(i)
    time.sleep(0.01)

def ReverseNum(Nums):
    print("Numbers from 50 to 1 in reverse order ")
    for i in range(50,0,-1):
        print(i)
    time.sleep(0.01)


def main():
    thread1 = threading.Thread(target=SerialNum,args=(51,))
    thread1.start()
    thread1.join()

    thread2 = threading.Thread(target=ReverseNum,args=(1,))
    thread2.start() 
    thread2.join()
    

if __name__ == "__main__":
    main()