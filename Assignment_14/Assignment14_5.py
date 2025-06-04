class BankAccount:
    def __init__(self,account_num,account_name,account_balance):
        self.Acnt_Num = account_num
        self.Name = account_name
        self.Balance = account_balance

    def deposit(self,value):
        self.Balance += value 
        return self.Balance


    def Withdraw(self,value):
        self.Balance -= value
        return self.Balance

    def DisplayBalance(self):
        print(f"Available Amount: {self.Balance}")


def main():

    obj = BankAccount(101,"Aditi",1000)
    print("Deposited Amount: ",obj.deposit(100))
    print("Withdraw Amount: ",obj.Withdraw(200))

    obj.DisplayBalance()

if __name__ == "__main__":
    main()