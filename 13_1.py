m1=[[10,20,30],[40,50,60],[70,80,90]]
m2=[[15,30,45],[60,75,90],[85,95,100]]
m3=[[0,0,0],[0,0,0],[0,0,0]]

print("Addiion of two matrices is: ")
for i in range(len(m1)):
    for j in range(len(m2)):
        m3[i][j]=m1[i][j]+m2[i][j]
    for i in m3:
        print(i)

print("Subtraction of two matrices is: ")
for i in range(len(m1)):
    for j in range(len(m2)):
        m3[i][j]=m1[i][j]-m2[i][j]
    for i in m3:
        print(i)

print("Multiplication of two matrices is: ")
for i in range(len(m1)):
    for j in range(len(m2)):
        m3[i][j]=m1[i][j]*m2[i][j]
    for i in m3:
        print(i)

print("Division of two matrices is: ")
for i in range(len(m1)):
    for j in range(len(m2)):
        m3[i][j]=m1[i][j]/m2[i][j]
    for i in m3:
        print(i)

print("Performed by Parth and Dhruv")