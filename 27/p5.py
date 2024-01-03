stings = "abcdefghijklmnopqrstuvwxyz"
flag = True
strr = "A brown fox jumps over the lazy dog and Dies"
strr = strr.replace(" ","").lower()

for char in strr:
    if char not in stings:
        flag  = False
        break
print(flag)