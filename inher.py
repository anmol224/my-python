class a:
    def name(self):
        print("anmol")

    def __init__(self):
        print("constructor A")


class b():
    def init__(self):
        super().__init__();
        print("constructor b")
        super().name();


class c(a,b):
    def __init__(self):

        print("constructor c")
        super().__init__()
        super().name()



c1=c();
