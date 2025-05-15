Data = []
print("Enter the elememts: ")
Size = int(input())

print("Enter the Numeric Values: ")
for i in range(Size):
    no = int(input())
    Data.append(no)

print("Input Data: ",Data)

sum = 0
for i in Data:
    sum = sum + i
    
print("Addition of the elements is: ",sum)

