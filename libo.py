import numpy as np
# a=np.array([1,2,3])
# print(type(a))
# print(a.shape)
# b=np.arange(12)
# print(b)
# b.reshape(3,4)
# print(b)
#b=np.arange(12).reshape(3,4)
#print(b)

#import scipy
# from scipy import constants
# print(constants.c)
# print(constants.h)
# print(constants.N_A)

import pandas as pd
# df = pd.DataFrame(np.random.randn(6,4),index=list(range(6)),columns=list('ABCD'))
# print(df)
# print(df.describe())

# import matplotlib.pyplot as plt

# np.random.seed(10)

# N=30
# x=np.random.rand(N)
# y=np.random.rand(N)
# colors=np.random.rand(N)
# area=(150*np.random.rand(N)**2)
# plt.scatter(x,y,s=area,c=colors,alpha=0.4)
# plt.show()

import sys
import time
# b=range(1000)
# print(sys.getsizeof(5)*len(b))
# d=np.arange(1000)
# print(d.size*d.itemsize)

# size=100000
# L1=range(size)
# L2=range(size)

# A1=np.arange(size)
# A2=np.arange(size)

# start=time.time()
# res=[(x+y) for x,y in zip(L1,L2)]
# res=[(x+y) for x,y in zip(L1,L2)]
# print(res)
# print('python list took: ',(time.time()-start)*1000)

# start=time.time()
# res1=A1+A2
# print(res1)
# print('numpy array took: ',(time.time()-start)*1000)

#arr=np.array([[1,2],[3,4],[5,6]])
# print(arr)
# print(arr.ndim)
# print(arr.itemsize)
# print(arr.shape)

#print(np.zeros((3,4)))
#print(np.ones((3,2),dtype=np.complex128))

#print(pd.__version__)

# arr=[10,23,40,67.88]
# s1=pd.Series(arr)
# print(s1)

#assigning index to numpy array elements
# g=np.random.randn(5)
# ind=['1','2','3','d','e']
# s1=pd.Series(g,index=ind)
# print(s1)

#Series Op
# arr=[0,1,2]
# arr1=[4,5,6]
# s5=pd.Series(arr)
# s6=pd.Series(arr1)
# print(s5)
# print(s6)
# print(s5.add(s6))
# print(s5.median())
# print(s6.median())
# print(s5.max())
# print(s6.max())
# print(s5.min())
# print(s6.min())

#Create DataFrame
#dts=pd.date_range('today',periods=7)
#print(dts)
# nm_arr=np.random.randn(7,4)
# clms=['A','B','C','D']
# df1=pd.DataFrame(nm_arr,index=dts,columns=clms)
# print(df1)

datas={'animal':['cat','cat','dog','dog','tiger','tiger','dog','tiger','lion','dog'],
      'age':[2.5,3,2,3.3,2,2,5.4,5,6.2,6.1],
      'visits':[1,1,2,2,3,4,5,6,3,2],
      'priority':['yes','yes','yes','yes','no','no','no','no','yes','no']}

labels=['a','b','c','d','e','f','g','h','i','j']

df2=pd.DataFrame(datas,index=labels)
#print(df2)
#print(df2.describe())
#print(df2.T)
#print(df2.sort_values(by='age'))
#print(df2[1:3])
#print(df2[['age','visits']])
df3=df2.copy()
# print(df3.isnull())
df3.loc['f','age']=9
#print(df3)
#print(df3.mean())
#print(df3['visits'].mean())
#print(df3.sum())
# strng=pd.Series(['a','b','Lop',23,9.76,np.nan])
# print(strng.str.upper())
# print(strng.str.lower())
# print(df2)
# print("\n\n")
# print(df3)
#df3.to_csv('animaldf3.csv')
#df3.to_excel('animaldf3.xlsx')