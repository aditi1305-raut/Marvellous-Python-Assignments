print("Enter a Number: ")
num = int(input())

for i in range(2,num+1):
    
    if (num % i == 0):
        print(f"Number {num} is not Prime ")
        break

    else:
        print(f"Number {num} is Prime")
        break