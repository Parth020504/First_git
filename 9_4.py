data = {"V":"S001", "V": "S002", "VI": "S001", "VI": "S005","VII":"S005", "V":"S009", "VIII":"S007"}
print ("Original Dictionary : ",data)
print ("Unique values : ",end="")
a = list(data.values())
for value in a:
    if a.count(value)<=1:
        print(value,end="   ")
print("Performed by Parth and Dhruv")
