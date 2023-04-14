class sample:
    def __init__(self):
        print("This is a constructor")

    def __del__(self):
        print("This is a destructor")
print("This is outside the class")

a= sample()
a.__init__()
a.__del__()
