class Student:
    School_Name = "Old School"

    def __init__(self,name,roll_no):
        self.Name = name
        self.Roll_No = roll_no


    def Display(self):
        print(f"Name: {self.Name}")
        print(f"Roll No : {self.Roll_No}")


def main():
    obj = Student("Aditi",13)

    print("School Name: ",Student.School_Name)
    Student.School_Name= "New School"
    print("School Name: ",Student.School_Name)

    obj.Display()

if __name__ =="__main__":
    main()
