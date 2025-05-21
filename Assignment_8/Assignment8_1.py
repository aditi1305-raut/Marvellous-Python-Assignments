import threading

def Even(value1,value2):
    print("Even Numbers: ")
    for no in range(value2+1):
        if (no%2==0):
            print(no)


def Odd(value1,value2):
    print("Odd Numbers: ")
    for no in range(value2+1):
        if (no%2 != 0):
            print(no)

def main():
     T1 = threading.Thread(target=Even,args=(1,21))
     
     T2 = threading.Thread(target=Odd,args=(1,21))
     
     T1.start()
     T2.start()

     #T1.join()
     #T2.join()


if __name__ =="__main__":
    main()





