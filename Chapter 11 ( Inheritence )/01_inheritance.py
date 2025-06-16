
class Employee :
    company = "ITC"
    def show(self):
        print(f"Emp name {self.name} emp salary is {self.salary}")

# class Programmer :
#     company = "ITC"
#     def show(self):
#         print(f"Emp name {self.name} emp salary is {self.salary}")
    
#     def showLanguage(self):
#         print(f"Emp name {self.name} emp is good with {self.language} language")

# By using inheritence

class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        
        print(f"Emp name {self.name} emp is good with {self.language} language")





a = Employee()
b = Programmer()
print(a.company,b.company)