name = ("one","two","three","four","five","six","seven","eight","nine")
n = int(input("Enter a number : "))
temp = n
n = ()
while temp > 0:
    d = temp%10
    n+=(d,)
    temp=temp//10
n = n[::-1]
for i in n :
    print(name[i-1],end="")