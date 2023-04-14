# class student:
#     def take(self,a,g):
#         self.age=a
#         self.gender=g 

#     def show(self):
#         print("Age: ",self.age)
#         print("Gender: ",self.gender)

# s1=student()
# s2=student()
# s1.take("20","Male")
# s2.take("18","Female")
# s1.show()
# s2.show()

class test:
    x=5
    y=10
    def show(self):
        print("X= ",self.x)
        print("Y= ",self.y)
t=test()
t.show()
del test.x
print("X= ",t.x)