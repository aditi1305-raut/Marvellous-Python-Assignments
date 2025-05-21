
result = 1
def Power(num1 , num2):
    global result
    
    if(num2>0):
        result = num1*result
        num2 = num2 -1
        Power(num1,num2)

    return result

def main():
    ret = Power(2,3)
    print(ret)


if __name__ == "__main__":
    main()