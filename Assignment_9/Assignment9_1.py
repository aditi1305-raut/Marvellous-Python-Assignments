import threading
import time

def DisplayNum(nums):
    
    for i in range(1,nums+1):
        print(i)
    time.sleep(1.0)



def main():
    
    thread1 = threading.Thread(target=DisplayNum , args=(5,))
    

    thread2 = threading.Thread(target=DisplayNum , args=(5,))
    

    thread3 = threading.Thread(target=DisplayNum , args=(5,))
    

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()

    thread3.start()
    thread3.join()


if __name__ =="__main__":
    main()