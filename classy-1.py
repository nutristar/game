class Table:
    d=1
    w=1
    s=0

    def setW(self,fw):
        self.w=fw

    def setD(self, fd):
        self.d = fd
    def square (self):
        self.s=self.w*self.d


v=Table()
print(v.d)
print(v.w)
print(v.s)
v.setW(10)
v.setD(5)
v.square()
print(v.s)
