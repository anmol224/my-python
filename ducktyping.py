# here we will use ducktyping which implements polymorphism
# in duck typing it does not matter which class object you are using
# only matters is that object should have that method you are calling
class lion:
    def behave(self):
        print("this animal roars")

class  computer:
    def behave(self):
        print("hii this is computer")

class laptop:
    def show(self,oth):
        print("hii iam laptop")
        oth.behave()
lp=laptop()
com=computer()
ln=lion()
lp.show(com)
lp.show(ln)
