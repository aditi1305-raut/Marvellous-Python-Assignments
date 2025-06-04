class Employee:

    def __init__(self,name,department,salary):
        self.Name = name
        self._dept = department
        self.__Salary = salary

    def Show(self):
        print(f"Name: {self.Name}")
        print(f"Department: {self._dept}")
        print(f"Salary: {self.__Salary}")


def main():

    obj = Employee("Aditi","Machine Learning", 60000)

    obj.Show()

    print(obj.Name)
    print(obj._dept)
    #print(obj.__Salary)         #Error: Private 

    print(obj._Employee__Salary)        #Accessing Private via Name Mangling

if __name__ == "__main__":
    main()

