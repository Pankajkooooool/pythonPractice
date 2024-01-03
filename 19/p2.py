fruits= []
while True:
    f = input("Enter fruit name , X to stop")
    if f == 'X':
        break
    else:
        fruits.append(f)
        
with open("fruits.txt","w") as file :
    for fruit in fruits:
        file.write(f"{fruit}\n")