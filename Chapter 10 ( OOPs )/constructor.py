
class Employee :
    language = "python"
    salary = 120000

    def __init__(self,name,salary,language):  # dudner methods which are called automatically
        self.name = name
        self.salary = salary
        self.language = language

        print("I am creating an Object")

    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")
    
    @staticmethod 
    def greet(self):
        print("Good Morning")

harry = Employee("Atharva",9000000,"JAVA") 
print(harry.language, harry.salary , harry.name)
