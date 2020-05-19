# here we will define and use lambda function
# lambda functions are single expression functions
# lambda function are also called anonymous functions

j=lambda a:a*a

print(j(5))
# using lambda functions in filters
# filter functions we use to filter out the values from a bunch of values
ls=[12,23,4,5,6,7,9]
odds=list(filter(lambda n:n%2!=0,ls))
print("using filter",odds)
# map functions we use to operate on data and obtain the result
l=list(map(lambda n:n*3,odds))
print("using map",l)
#reduce functions are use to reduce to a value by operating on set of values
from functools import reduce
ls=[12,1,34,56,78,99]
s=reduce(lambda a,b:a+b,ls)
print("using reduce",s)