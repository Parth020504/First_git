def fact(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    print("Factorial of number is ",factorial)
num=int(input("Enter a number: "))
fact(num)
print("Performed by Parth and Dhruv")