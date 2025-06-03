class Arithmatic:
    def __init__(self,value):
        self.Value = value

    def ChkPrime(self):
        if self.Value < 2:
            return False
        
        for i in range(2,self.Value):
            if self.Value % i == 0:
                return False
        return True
    
    def ChkPerfect(self):
        Sum = 0 

        for i in range(1,self.Value):
            if self.Value % i == 0:
                Sum = Sum + i
        
        return sum == self.Value
    
    def Factors(self):
        print("Factors are: ")

        for i in range(1 , self.Value+1):
            
            if self.Value % i == 0:
                print(i)

    def SumFactors(self):
        sum = 0 

        for i in range(1,self.Value ):
            if self.Value % i == 0:
                sum = sum + i

        return sum
    

def main():
    
    print("Enter a Number: ")
    num = int(input())
    
    obj = Arithmatic(num)
    
    print(" whether a Prime Number? : ",obj.ChkPrime())

    print(" whether a Perfect Number? : ",obj.ChkPerfect())

    obj.Factors()

    print("Sum of Factors: ",obj.SumFactors())


if __name__ == "__main__":
    main()