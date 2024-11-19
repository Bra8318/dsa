'''import array as arr
a = arr.array('i',[x for x in range(10)])
a.append(10)
a.extend([11,12,13,14])
a.insert(3,15)
a.pop(6)
x = a.pop()
print(x)

b = arr.array('i',[16,17,18])
c = arr.array('i',[19,20,21])
d = a+b+c
print("concatenated array ",d)

print("concatenated array lentgh ",len(d))

print(d[8])
print(a)'''


'''import array as arr
a = arr.array('i',[])
length = 5
for i in range(length):
    b = eval(input("enter a number:"))
    a.append(b)
print(a)'''

'''import numpy as np
arr = np.array([[2,4],[6,8]])
print("Data Type: ",arr.dtype)
print("Rank of a Matrix: ",arr.ndim)
print("Order of Matrix: ",arr.shape)
print("Convert 2D into 1D: ",arr.flatten())

arr1 = np.array([[1,3],[5,7]])
print("add of two matrix:\n",arr+arr1)
print("subtraction of two matrix:\n",arr-arr1)
print("multiple of two matrix:\n",arr.dot(arr1))
print("division of two matrix:\n",arr/arr1)'''


'''import numpy as np
arr = np.arange(1,10)
arr1 = arr.reshape(3,3)
print("Transpose of a Matrix:\n",arr1.T)

a = np.arange(1,10)
arr2 = a.reshape(3,3)
print("multiple of two matrix:\n",arr1.dot(arr2))'''










