import datetime
time = datetime.datetime.now().time()

name = input("Name ? : ")

def func(name):
    if(time <datetime.time(12,0)):
        greeting = "Good Morning"
    elif(time <datetime.time(17,0)):
        greeting = "Good Afternoon"
    else : 
        greeting = "Good Evening"
    return f"{greeting}, {name}"
print(func(name))