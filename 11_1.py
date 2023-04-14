def fun(n):
    for i in range(2,n+1):
        if n%i==0:
            break
    if i==n:
        print(n," is a Prime number")
    else:
        print(n," is not a prime number")
n=int(input("Enter a number: "))
fun(n)
print("Performed by Parth and Dhruv")