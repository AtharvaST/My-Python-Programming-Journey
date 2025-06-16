
words = ["Donkey" , "bad", "ganda"]
# To open and get content from file
with open("p4.txt" , "r") as  f :
    content = f.read()
for word in words :
    content = content.replace(word , "#"*len(words))

# To write content in file 
with open("p4.txt" , "w") as  f :
    content = f.write(content)