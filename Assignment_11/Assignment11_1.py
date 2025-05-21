

def Numbers(no):
    
    if (no>=1):
        no = no -1
        Numbers(no)
        print(no+1) 
           

def main():
    print("Enter a Number: ")
    Nums = int(input())
    
    ret = Numbers(Nums)
    print(ret)


if __name__ == "__main__":
    main()


