class Employee :
    a = 1
    @classmethod    
    def show(cls):
        print(f"The value of attribute of a is : {cls.a}")
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

o = Employee()
o.a = 45 

o.name = "Atharva Teli"
print(o.fname , o.lname)
o.show()