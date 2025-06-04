class Person:
    def __init__(self,name,age):
        self.Name = name
        self.Age = age

    def Display(self):
        print(f"Name: {self.Name} , Age: {self.Age}")


class ClassTeacher(Person):
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.Subject = subject
        self.Salary = salary
        
    def Display(self):
        super().Display()
        print(f"Subject: {self.Subject} , Salary: {self.Salary}")

def main():

    obj = ClassTeacher("Aditi",22,"Maths",50000)
    obj.Display()



if __name__== "__main__":
    main()

