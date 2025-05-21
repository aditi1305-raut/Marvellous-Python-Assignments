import threading

def Small(chars):
    count = 0
    for char in chars:
        if char.islower():
           count = count + 1
    print("Number of Lower characters are: ",count)
    print("Thread ID: ",threading.get_ident())


def Capital(chars):
    count = 0
    for char in chars:
        if char.isupper():
           count = count + 1
    print("Number of Lower characters are: ",count)
    print("Thread ID: ",threading.get_ident())


def digits(chars):
    count = 0
    for char in chars:
        if char.isdigit():
          count = count + 1
    print("Number of Lower characters are: ",count)
    print("Thread ID: ",threading.get_ident())



def main():
    print("Enter a String: ")
    word = input()

    T1 = threading.Thread(target = Small,args=(word,))
    T1.start()

    T2 = threading.Thread(target = Capital,args=(word,))
    T2.start()

    T3 = threading.Thread(target = digits,args=(word,))
    T3.start()

    T1.join()
    T2.join()
    T3.join()


if __name__ == "__main__":
    main()