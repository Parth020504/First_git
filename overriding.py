# # class boi:
# #     def roi(self):
# #         return 10
    
# # class sbi(boi):
# #     def roi(self):
# #         return 15
    
# # class bob(boi):
# #     def roi(self):
# #         return 20
    
# # a=boi()
# # b=sbi()
# # c=bob()

# # print("BOI: ",a.roi())
# # print("SBI ",b.roi())
# # print("BOB: ",c.roi())

# class boy:
#     def show(self,n):
#         self.name=n 
#         print("The name is ",self.name)

#     def isboy(self):
#         return True

# class girl(boy):
#     def disp(self,n):
#         self.name=n
#         print("The name is ",self.name)

#     def isboy(self):
#         return False

# a=boy()
# a.show("Parth")
# print(a.isboy())

# b=girl()
# b.disp("Ritika")
# print(b.isboy())

class Animals:
    a="Cow"
    def animal(self):
        print("This is Animals class")
        
class Feed(Animals):
    b="Grass"
    def animal(self):
        print("This is over ridden class")

a1=Animals()       
a2=Feed()
a1.animal()

print("The Animal is: ",a1.a)
print("They feed on: ",a2.b)
