class employee:
    name=""
    dept=""
    salary=""
    def accept(self):
        print("Reading the details from user: ")
        print("Enter the name:")
        self.name=input()
        print("Enter the department:")
        self.dept=input()
        print("Enter the salary:")
        self.subject=input()
    
    def show(self):
        print("Name of the employee: ",self.name)
        print("Department of the employee: ",self.dept)
        print("Salary of the employee: ",self.salary)

s1=staff()
# s2=staff()
# s3=staff()

s1.accept()
# s2.accept()
# s3.accept()

s1.show()
# s2.show()
# s3.show()