class Arithmatic:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        print("Enter first Value: ")
        self.value1 = int(input())

        print("Enter Second Value: ")
        self.value2 = int(input())

    def Addition(self):
        Add = self.value1 + self.value2 
        return Add
    
    def Subtraction(self):
        Sub = self.value1 - self.value2 
        return Sub
    
    def Multiplication(self):
        Mult = self.value1 * self.value2
        return Mult

    def Divison(self):
        Div = self.value1 / self.value2 
        return Div

def main():
    obj = Arithmatic()

    obj.Accept()
    print("Addition: ",obj.Addition())
    print("Subtraction: ", obj.Subtraction())
    print("Multiplication: ",obj.Multiplication())
    print("Divison: ",obj.Divison())

if __name__ == "__main__":
    main()