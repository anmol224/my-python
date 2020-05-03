class student:
    def marks(self,m1,m2):
        self.m1=m1;
        self.m2=m2;

    def mdetails(self):
        print(self.m1,self.m2)

    class laptop:
            def __init__(self,m):
                self.ram=m
                self.name='hp'

            def show(self):
                print(self.name,self.ram)

s1=student()
s2=student()
s1.marks(12,24);
s1.mdetails();
s2.marks(23,24)
s2.mdetails()
lap1=student.laptop(240);
print(id(lap1))
lap1.show();


