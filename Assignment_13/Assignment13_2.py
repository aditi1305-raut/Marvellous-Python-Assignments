class BankAccount:

    ROI = 10.5

    def __init__(self,name,amount):
        self.Name = name
        self.Amount = amount


    def Deposit(self,Value):
        self.Amount += Value

    def Withdraw(self,Value):
        self.Amount -= Value

    
    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI)/100
        return interest
    
    def Display(self):
        print(f" Name : {self.Name} and Available Amount: {self.Amount}")


def main():

    print("Enter the Accounter Name: ")
    name1 = input()

    print("Enter the Amount: ")
    money = float(input())

    acc = BankAccount(name1,money)
    acc.Deposit(500)
    acc.Withdraw(200)
    print(f"Interest: {acc.CalculateInterest()}")
    acc.Display()


if __name__ == "__main__":
    main()