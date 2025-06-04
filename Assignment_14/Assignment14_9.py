class Product:

    def __init__(self,name,price):
        self.Name = name
        self.Price = price

    def __eq__(self,other):
        return self.Price == other.Price
    
def main():

    P1 = Product("Mobile",20000)
    P2 = Product("Watch",50000)

    print(P1 == P2)


if __name__ =="__main__":
    main()