# operator overloading
# when we perform any operation like +,-,*,/ are all performed by calling a function which is behind


class student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):  # this is  for addition operation
        r1 = self.m1 + other.m1
        r2 = self.m2 + other.m2
        return "{} {}".format(r1, r2)

    def __gt__(self, other):  # this is  for greater than operation
        return False

    def __str__(self):  # this is for print operation
        return '{} {}'.format(self.m1, self.m2)

    def __mul__(self, other):  # this is for multiplication
        q1 = self.m1 * other.m1
        q2 = self.m2 * other.m2
        return "{} {}".format(q1, q2)

    def __le__(self, other):  #this is for less than or equal to operation
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 >= r2:
            return True
        else:
            return False


s1 = student(89, 88)
s2 = student(89, 88)
s3 = s1 + s2
print(s3)
if s1 > s2:
    print("s1 gets more marks")
else:
    print("s2 gets more marks")
print(s1)

s4 = student(12, 12)
s5 = student(12, 12)
s6 = s5 * s4
print(s6)
stu1 = student(90, 87)
stu2 = student(90, 87)
if stu1 <= stu2:
    print("yes both are equal")
else:
    print("no they are different")
