#Write a Recursive Function to calculate the Sum of digits of a Number

#Error 
sum = 0

def Addition(num):
    global sum 
    
    if(num>=1):
        sum = sum + num
        
        num = num -1
        Addition(num)

    return sum

def main():
    result = Addition(5)
    print(result)

if __name__ == "__main__":
    main()