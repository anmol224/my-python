import numpy as n
arr=n.array([1,2,0,4],'i')
print(arr)

print(arr.dtype)
newarr=arr.astype(float)
print(newarr)
print(newarr.dtype)

no=arr.astype(bool)
print(no)
print(no.dtype)
# copy and view
ar=n.array([1,2,3,4,5])
x=ar.copy()
ar[1]=23
print(ar)
print(x)
y=ar.view()
print(ar)
ar[2]=12
print(y)
print(x.base)
print(y.base)
print(x.shape)
