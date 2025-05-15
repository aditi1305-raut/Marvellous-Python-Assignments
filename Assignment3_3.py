Data = []
print("Enter the Number of elements: ")
Size = int(input())

print("Enter the numeric values : ")
for i in range(Size):
    no = int(input())
    Data.append(no)

print("Input Data: ",Data)

print("Minimum From List: ",min(Data))