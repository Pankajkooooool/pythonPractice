string1 = "Pankaj"
string2 = "jaPnka"
flag = True

for ch in string1:

   if ch not in string2:
       flag = False
       break
print(flag)
    