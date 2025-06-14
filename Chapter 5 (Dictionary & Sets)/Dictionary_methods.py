marks = {
    "Atharva" : 100,
    "Hanni" : 54,
    "Minji" : 98,
    "Momo" : 79,
    "list" : [23,"Sana",True],
    0 : "Rohan"
}
# print(marks.items())  # gives all key value pairs

print(marks.keys())  # gives only key values.
print(marks.values())  # gives only values of key.

# update value in dict
marks.update({"Atharva" : 97 , "Danielle" : 100}) # We can also add new values using this function
print(marks)

# get function
print(marks.get("Atharva"))
print(marks.get("Atharva2")) # its gives none
print(marks["Atharva2"]) # its gives an error 