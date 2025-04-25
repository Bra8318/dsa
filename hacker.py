import numpy as np 
n,m = input().split()
array = []
for i in range(int(n)*2):
    a = list(map(int,input().split()))
    array.append(np.array(a,ndmin=2,dtype = int))
a = array[0].copy()
s = array[0].copy()
m = array[0].copy()
d = array[0].copy()
mo = array[0].copy()
p = array[0].copy()
for j in range(1,len(array)):
    a += array[j]
    s -= array[j]
    m *= array[j]
    d //=array[j]
    mo %= array[j]
    p **= array[j]
print(a)
print(s)
print(m)
print(d)
print(mo)
print(p)



