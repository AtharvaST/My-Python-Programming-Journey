

class Employee :
    company = "ITC"
    name = "Don"
    def show(self):
        print(f"Emp name {self.name} emp salary is {self.company}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language : {self.language}")

# By using Multiple inheritence

class Programmer(Employee,Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} emp is good with {self.language} language")


a = Employee()
b = Programmer()
b.show()
b.showLanguage()
b.printLanguages()