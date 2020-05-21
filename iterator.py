# iterating through list
# for loop also calls next in-built method while iterating
ls=[12,23,45,67,89]
itr=iter(ls)
print(itr.__next__())
print(next(itr))


# creating our own iterator object usinf inbuilt __iter__ and __next__ fucntions
class myiterator:
    def __init__(self):
        self.n=1
    def  __iter__(self):
        return self
    def __next__(self):
        if self.n<=10:
            val=self.n
            self.n+=1
            return val
        else:
            raise StopIteration

it=myiterator()
print(next(it))
for i in it:
    print(i)