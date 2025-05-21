
fact = 1
def Factorial(num):
    global fact
    if (num>=1):
        fact = fact * num
        num = num -1 
        Factorial(num)

    return fact

def main():
    ret = Factorial(5)
    print(ret)


if __name__ == "__main__":
    main()
