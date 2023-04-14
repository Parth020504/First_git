class add:
    def __init__(self,f,s):
        self.first=f
        self.second=s
    
    def take(self):
        print("The first number is ",self.first)
        print("The second number is ",self.second)
        print("The sum is ",self.res)
    
    def cal(self):
        self.res=self.first+self.second

a1=add(20,30)
a1.cal()
a1.take()
