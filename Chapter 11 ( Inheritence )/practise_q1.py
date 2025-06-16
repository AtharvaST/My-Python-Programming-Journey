
class towDVector : 
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"The Vector is {self.i}i + {self.j}j")

class threeDVector(towDVector): 
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    def show(self):
        print(f"The Vector is {self.i}i + {self.j}j + {self.k}k")


a = towDVector(1,2)
# print(a.i , a.j)
a.show()
b = threeDVector(1,2 ,3) 
# print(b.i , b.j , b.k)
b.show()
