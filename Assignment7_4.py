from functools import reduce

Product = lambda A , B : (A*B)

Data = []

print("Enter the Number: ")
Size = int(input())

print("Enter the Numeric Values: ")
for no in range(Size):
    no = int(input())
    Data.append(no)

print("Input Data: ",Data)

RData = reduce(Product,Data)
print("Product: ",RData)

