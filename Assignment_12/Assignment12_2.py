class Circle:
    PI = 3.14

    def __init__(self ):
        self.radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        print("Enter the Radius: ")
        self.radius = float(input())


    def CalculateArea(self):
        self.Area = Circle.PI * self.radius * self.radius
        

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.radius

    def Display(self):
        print("Radius of Circle is: ",self.radius)
        print("Area of Circle: ",self.Area)
        print("Circumference of Circle: ",self.Circumference)

def main():
    obj = Circle()
    obj.Accept()
    obj.CalculateArea()
    obj.CalculateCircumference()
    obj.Display()


if __name__ == "__main__":
    main()


