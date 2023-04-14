def cal(str):
    l=0
    u=0
    for value in str:
        if(value.islower()):
            l+=1
        else:
            u+=1
    print("Number of lower case characters ",l)
    print("Number of upper case characters ",u)
str=input("Enter a string: ")
cal(str)
print("Performed by Parth and Dhruv")