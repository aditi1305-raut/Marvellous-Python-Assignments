print("Enter a Number: ")
no = int(input())

Square = lambda no : no**2

ret = Square(no)

print("Square : ",ret)

Cube = lambda no : no ** 3

ret = Cube(no)

print("Cube: ",ret)