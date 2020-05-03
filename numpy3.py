import numpy as n
# reshaping of array
ar=n.array([1,2,3,4,5,6,7,8])
print(ar)
x=ar.reshape(2,4)
print(x)
print(x.base)
y=ar.reshape(2,2,2)
print(y)
z=y.reshape(-1)
print(z)
# iterating  through arrays
arr=n.array([[1,2,3],[4,5,6]])
for x in arr:
    for y in x:
        print(y)
aq=n.array([1,2,3,4,5],ndmin=3)
print(aq)
for x in aq:
    for y in x:
        for q in y:
            print(q)
for x in n.nditer(aq):
    print(x)

ar=n.array([[1,2,3],[4,5,6]])
print(ar[0:2,1:3])
print(ar[:,::2])
for i, x in n.ndenumerate(ar):
    print(i,x)
w=n.array([1,2,3],ndmin=3)
for y ,j in n.ndenumerate(w):
    print(y,j)
a=n.array([1,2,3,4,5])
for t,y in n.ndenumerate(a):
    print(y,t)