from array import *
# arr=array('i',[1,2,3,4,5])
# print(type(arr))
# print(arr[0])
# print(arr[2])

#for loop in array to print elements
#for j in arr:
    #print(j,end=' ')
    # try:
    #  print(arr[j])
    # except:
    #    #print('error handled')
    #    print(arr[j])

#pointer for loop 
#for pnt in range(5):
    #print(arr[pnt],end=" ")

# for jkl in range(0,5):
#     print(jkl,arr[jkl])

#reversing an array using .reverse() method
# arr.reverse()
# print(arr)

#reversing an array using slicing
# rev=arr[::-1]
# print(rev)

#.append()
# arr.append(10)
# print(arr)

#.remove()
# arr.remove(2)
# print(arr)

# arr[2]=2
# print(arr)
# arr.remove(2)
# print(arr)

#array created by user inputs
arr=array('i',[])
x=int(input('enter array size: '))
print('enter %d elements' %x)
for i in range(x):
    n=int(input())
    arr.append(n)
print(arr)