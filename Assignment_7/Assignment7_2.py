Double = lambda no : (no * 2)

Data = []

print("Enter the Number of Elements: ")
Size = int(input())

print("Enter the Numeric Values: ")
for no in range(Size):
    no = int(input())
    Data.append(no)

print("Input Data: ",Data)

MData = list(map(Double,Data))
print("Doubled List: ",MData)