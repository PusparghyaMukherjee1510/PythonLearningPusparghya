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

