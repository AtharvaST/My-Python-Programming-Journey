
class Employee :
    a = 1
    @classmethod    
    def show(cls):
        print(f"The value of attribute of a is : {cls.a}")

o = Employee()
o.a = 45 # here class method is used so it will not show 45 it will show attribute as delcared in class itself ( it woudnt change)
o.show()