class add:
    def sum(self,a,b):
        return a+b 

class sub:
    def diff(self,a,b):
        return a-b
    
class mul(add,sub):
    def prod(self,a,b):
        return a*b
    
m=mul()
print("The addition is ",m.sum(20,5))
print("The difference is ",m.diff(20,5))
print("The product is ",m.prod(20,5))
