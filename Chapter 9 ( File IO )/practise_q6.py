with open("log.txt",) as f:
    content = f.read()

if("Python" in content):
    print("Yes Python word is present")
else:
    print("NO Python word is not present")

    

