
word = ["Donkey","bad","ganda"]
# To open and get content from file
with open("p4.txt" , "r") as  f :
    content = f.read()
contentNew = content.replace(word , "######")

# To write content in file 
with open("p4.txt" , "w") as  f :
    content = f.write(contentNew)