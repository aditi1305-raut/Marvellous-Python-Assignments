class Rectangle:

    def __init__(self,length,width):
        self.Length = length
        self.Width = width

    def ComputeArea(self):
        return self.Length * self.Width
    
    def ComputePerimeter(self):
        return 2*(self.Length + self.Width)
    
def main():

    obj = Rectangle(10,20)

    print("Area of Rectangle: ",obj.ComputeArea())

    print("Perimeter of Rectangle: ",obj.ComputePerimeter())


if __name__ == "__main__":
    main()