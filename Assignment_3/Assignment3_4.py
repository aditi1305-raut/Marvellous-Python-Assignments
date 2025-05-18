
Data = []
print("Enter the Number of elements: ")
Size = int(input())

print("Enter the numeric values : ")
for i in range(Size):
    no = int(input())
    Data.append(no)

print("Input Data: ",Data)

unique = set(Data)

print("Enter the Number to Search: ")
list_num = int(input())

for num in unique:
    if (list_num == num):
        print("Frequency of Number is: ",Data.count(list_num))
    
    #print(num,"appears",Data.count(num),"times")
    