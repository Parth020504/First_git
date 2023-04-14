

# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# # print(arr.size)

# # new_arr=arr.reshape(2,3,2)
# # print(new_arr)
# arr3 = np.array([[1, 2], [3, 4], [9,10]])
# arr4 = np.array([[5, 6], [7, 8], [11,12]])
# arr7 = np.concatenate((arr3, arr4),axis=0)
# print(arr7)

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(3,2,2) 
# # 1st-no. of matrices 2nd-row 3rd-column
# print(newarr)

import matplotlib.pyplot as plt
# x=[2,4,6]
# y=[1,2,3]
# plt.plot(x,y)
# plt.show()

# x=[5,10,15,20]
# y=[20,40,60,80]

# plt.xlabel("No. of days")
# plt.ylabel("Marks")
# plt.bar(x,y,label="Graph",color='b',width=2.0)
# plt.show()

# y=[1,1,2,2,2,2,2,3,3,3,3,4,4,5]
# plt.hist(y)
# plt.show()

# x=[1,2,3,4,5,6]
# y=[4,3,8,10,2,7]
# plt.scatter(x,y)
# plt.show()

import pandas as pd
import numpy as np

# a=np.array([1.2,2,3,4,5,])
# index=['b','c','d','a','e']
# si=pd.Series(a,index)
# print(si)

# d={'a':0,'b':1,'c':2}
# s=pd.Series(d,index=['b','c','a','d'])
# print(s)

data = {
"calories": [420, 380, 390],
"duration": [50, 40, 45]
}
#load data into a DataFrame object:  df = pd.DataFrame(data)
df = pd.DataFrame(data)
print(df)  
print(df.loc[2])  
print(df[['calories']])

