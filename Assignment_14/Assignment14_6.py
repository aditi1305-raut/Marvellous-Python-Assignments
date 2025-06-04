class Calculator:
    def __init__(self,val1,val2):
        self.value1 = val1 
        self.value2 = val2

    def add(self):
        return self.value1 + self.value2
    
    def sub(self):
        return self.value1 - self.value2
    
    def multiply(self):
        return self.value1 * self.value2
    
    def divide(self):
        return self.value1/self.value2
    
def main():

    print("Enter a First Number: ")
    No1 = int(input())

    print("Enter a Second Number: ")
    No2 = int(input())

    ret = Calculator(No1 , No2)

    print("Addition: ",ret.add())

    print("Subtraction: ",ret.sub())

    print("Multiplication: ",ret.multiply())

    print("Divison: ",ret.divide())


if __name__ == "__main__":
    main()