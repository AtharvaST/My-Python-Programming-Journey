f = open("poem.txt")
content = f.read()
if("Twinkle" in content ):
    print("word twinkle is there in txt file")
else :
    print("word twinkle is not present in txt file")
f.close()