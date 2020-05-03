# ARRAYS USING NUMPY
# one dimensional array
import numpy as n
arr=n.array([1,2,3,4,5])
print(arr)
# two dimensional array
arr1=n.array([[1,2,3],[4,5,6]])
print(arr1)
# three dimensional array
arr2=n.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr2)
print(type(arr2))
#to check the dimensions of array
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
# you can create array by specifying dimension
ar=n.array([1,2,3,4,5],ndmin=5)

print(ar)
#  array indexing
print(arr[1]) #from one dimension
# now to access elements from 2 dimension
print(arr1[0,-2])
# now to access elements from 3 dimension
print(arr2[0,1,2])
# slicing of array
print(arr[1:3])
# now from 2d array
print(arr1[0:2,0:2])
print(arr2.shape)
print(arr1.shape)