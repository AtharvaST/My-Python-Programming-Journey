
class Employee :
    language = "python"
    salary = 120000
    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")
    
    @staticmethod # it means this below function doesnt need attributes property of class we just only need yo print
    def greet():
        print("Good Morning")

harry = Employee() 
harry.language = "JAVA"
# print(harry.language, harry.salary)
harry.greet()
harry.getInfo()
# Employee.getInfo()