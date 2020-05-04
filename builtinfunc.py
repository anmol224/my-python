#hello this programme contains all the built-in functions  of python
x=-12
# abs() function it returns the absolute value
print(abs(x))
# all() function it returns true if all items in an iterable are true
ls=[1,2,'apple']
print(all(ls))
# any() function it returns true if any item in an iterable is true
l=[1,0,'none','apple']
print(any(l))
# bin() it returns the binary form of a number
x=122
print(bin(x))
# bool() it returns value true if item is true otherwise false
x=0
print(bool(x))
# callable() it return true if an object is callable otherwise false
x=5
print(callable(x))
def x():
    pass
print(callable(x))
# delattr() it deletes the attributes of an object
class Python:
    age=199
delattr(Python,'age')
# dir() it returns all properties and methods even built in methods of an object
def python():
    pass
print(dir(python()))
#divmod() it returns the quotient and remainder
print(divmod(25,5))
#enumerate() it return a collection as a enumerate object
x=('apple','banana','orange')
y=enumerate(x,1)
print(list(y))
# filter() function it returns the iteratotr where values are filtered through a function
ar=[1,2,3,4,5]
def func(x):
    if x>3:
        return True
    else:
        return False

res=filter(func,ar)
print(list(res))
# format() function it is used to format the specifies value
x=format(25,'b')
print(x)
# frozenset() it freezes the iterable object and returns the unchangeable object
li=[1,2,3,4,5]
y=frozenset(li)
class a:
    age=20
    name="anmol"
x=getattr(a,'na',"name is not here")
print(x)
x=globals()
print(x["__file__"])
print(x)
#hasattr() it returns true if the object has specifird attribute
print(hasattr(a,'ae'))
x=int("245")
print(x)
# isinstance() it returns true if object is of specified type
print(isinstance(7,int))
#issubclass it returns true if  a specified class inherits from superclass
class a:
    pass
class b(a):
    pass
print(issubclass(b,a))
#map() it runs a specified function for each item in an itearble
def func(a):
    return len(a)
x=map(func,('anmol','b','bgjk'))
print(list(x))

#setattr() it sets the values of a specified attribute of an object
class a:
    age=30;

a1=a()
setattr(a,'age',20)
print(a1.age)
# slice() it returns the sliced object of a iterator or a sequence
ls=['apple','orange','mango','banana','1','2','3','5']
x=slice(1,6,2)
print(ls[x])
y=slice(3,8,3)
print(ls[y])
#sorted() it sorts the iterable object
x=[2,4,1,6,3]
print(sorted(x,reverse=False))
#zip() it joins two sequences
ls=[1,2,3,4,5]
la=[2,3,4,5,6]
x=zip(ls,la)
print(list(x))
print(sum(ls,9))