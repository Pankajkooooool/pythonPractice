temp = int(input("Enter the temperature you want to convert\t"))
choice = int(input("Choice 1: C to F \n 2: F to C\n"))

if choice == 1:
    res  = (temp * 9/5) + 32
    print(f"{temp} C = {res} F")
elif choice == 2:
    res = (temp - 32) * 5/9
    print(f"{temp} f = {res} C")
else : 
    print("invalid Choice")
    