
class Calculator:
    def __init__(self,n):
        self.n = n

    def Square(self):
        print(f"Square of Number is : {self.n*self.n} ")
    def Cube(self):
        print(f"Square of Number is : {self.n*self.n*self.n} ")
    def Squareroot(self):
        print(f"Square of Number is : {self.n**1/2} ")
    @staticmethod
    def greet():
        print("hello i am solution of practise_question_4")

        



a = Calculator(4)   
a.greet()
a.Square()
a.Cube()
a.Squareroot()