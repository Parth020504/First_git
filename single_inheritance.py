class base:
    def __init__(self,n):
        self.name=n
    
    def show(self):
        print("Hii ",self.name,". How are you??")

class derive(base):
    def disp(self):
        print("I am inside a derived class")

a=derive("Parth")
a.show()
a.disp()