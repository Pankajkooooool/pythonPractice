strin = "HEllo there I am pankaj"
v ,c =0,0
strin = strin.lower()
for char in strin: 
    if char == 'a' or char =='e' or  char =='i' or char =='o' or char =='u':
        v+=1
    else:
        c+=1
print(f'Vowels:{v},Consonants:{c}')