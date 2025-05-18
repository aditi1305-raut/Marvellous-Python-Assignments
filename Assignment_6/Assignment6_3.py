print("Enter a Number : ")
num = int(input())

mult = 1
for i in range(1,11):
    mult = num * i
    print(f"{num} * {i} = ",mult)