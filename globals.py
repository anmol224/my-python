# this program is about how we can change global variables

x=10 # global variable
def function():
    x=15
    return x
print("values of x in function()",function()) # prints 15 as x is local variable
print("global x",x) #prints 10 as x is global varaibla


def  change():
    global x   #changing global variable in function scope
    x=22
    print(x)

change()
print(x)
# now changing global variable without affecting local variable
z=20
def change():
    globals()['z']=10
    z=34
    print(z)

change() # changes global variable without affecting local one
print(z)
