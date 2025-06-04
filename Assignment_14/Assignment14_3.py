class Book:
    def __init__(self,price):
        self.__price = price

    def get_price(self):
        return self.__price
    
    def set_price(self,new_price):
        if new_price >=1:
            self.__price= new_price
            return new_price 

        else:
            print("Enter Invalid Value")
            #return new_price


def main():

    obj = Book(299)
    print("Initial Price : ",obj.get_price())

    #obj.set_price(350)
    print("Updated Price: ",obj.set_price(350))

    #obj.set_price(-50)
    print("Updated Price: ",obj.set_price(-50))


if __name__ == "__main__":
    main()