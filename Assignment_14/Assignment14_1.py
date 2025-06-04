class Employee:
    def __init__(self,name,emp_id,salary):
        self.Name = name
        self.ID = emp_id
        self.Salary = salary

    def Display(self):
        print(f"Name: {self.Name} ")
        print(f"ID: {self.ID}")
        print(f"Salary: {self.Salary}")

def main():

    obj = Employee("Rohit",101,50000)

    obj.Display()


if __name__ =="__main__":
    main()