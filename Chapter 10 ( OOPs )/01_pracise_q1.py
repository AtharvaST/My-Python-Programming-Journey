
class Programmer():
    company = "Microsoft"
    def __init__(self,name,language,salary):
        self.name = name
        self.language = language
        self.salary = salary

minji = Programmer("Hanni","java",1230000)
print(minji.name,minji.language,minji.salary,minji.company)
minji = Programmer("Momo","java",1230000)
print(minji.name,minji.language,minji.salary,minji.company)
minji = Programmer("Sana","java",1230000)
print(minji.name,minji.language,minji.salary,minji.company)

