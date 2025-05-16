def Prime(num):
    if num == 1:
        return False
    
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

Data = []

print("Enter the Number of Elements: ")
Size = int(input())

print("Enter the Numeric Values: ")
for num in range(Size):
    num = int(input())
    Data.append(num)

print("Input List: ",Data)

FData = list(filter(Prime,Data))
print("Prime Numbers: ",FData)
        
    