print("Enter the input number: ")
num = int(input())

Add = 0

for factor in range(1,num):
    if (num % factor == 0): 
        Add = Add + factor

print("Addition of number is : ",Add)
   