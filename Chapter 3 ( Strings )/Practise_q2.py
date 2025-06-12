letter = '''Dear <|Name|>,
You are selected!
<|Date|> '''

print(letter.replace("<|Name|>" , "Atharva").replace("<|Date|>" , "04 Sept 2025") )