strin = "HEllo World"

strin = strin.split()

piglatinwords =[]
for word in strin : 
    piglatinword = word[1:] + word[0].lower() + "ay"
    piglatinwords.append(piglatinword)
    
print(" ".join(piglatinwords))