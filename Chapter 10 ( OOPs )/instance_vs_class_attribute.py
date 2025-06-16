
class Employee :
    language = "python"
    salary = 120000

harry = Employee() # Here harry is object and above are its attributes  
harry.language = "JAVA"
print(harry.language, harry.salary)

'''
Instance attributes, take preference over class 
attributes during assignment & retrieval. 
So Java will be printed 
  '''               