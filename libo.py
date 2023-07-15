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

#import pandas as pd
# df = pd.DataFrame(np.random.randn(6,4),index=list(range(6)),columns=list('ABCD'))
# print(df)
# print(df.describe())

import matplotlib.pyplot as plt

np.random.seed(10)

N=30
x=np.random.rand(N)
y=np.random.rand(N)
colors=np.random.rand(N)
area=(150*np.random.rand(N)**2)
plt.scatter(x,y,s=area,c=colors,alpha=0.4)
plt.show()