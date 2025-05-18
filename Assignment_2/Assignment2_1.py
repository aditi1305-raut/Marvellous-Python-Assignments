import Arithmetic as A

print("Enter the First Number: ")
num1 =  int(input())

print("Enter The Second Number: ")
num2 = int(input())

sum = A.Add(num1 , num2)
print("The Addition is : ",sum)

subtract = A.Sub(num1,num2)
print("The Subtraction is: ",subtract)

mul = A.Mult(num1,num2)
print("The Multiplication is: ",mul)

divison = A.Div(num1,num2)
print("The Divison is: ",divison)


