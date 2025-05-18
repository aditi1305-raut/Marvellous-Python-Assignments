
Evens = lambda num: (num % 2 == 0) 

Data = []

print("Enter the Number of Elements: ")
Size = int(input())

print("Enter the Numeric Values: ")
for num in range(Size):
    num = int(input())
    Data.append(num)

print("Input List: ",Data)

FData = list(filter(Evens,Data))
print("Even Numbers: ",FData)