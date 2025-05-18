print("Enter the Number : ")
num = int(input())


for i in range(2,num):
    
    if (num % i== 0 ):
        print("The Number is  not Prime")
        break

    else:
        print("The Number is  Prime")
        break
            

