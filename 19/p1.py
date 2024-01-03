import random



b = random.randint(1,100)
points = 10
while True:
    a = int(input("Guess the Number (1 to 100)"))
    if a == b : 
        print(f'Yay you won, your score :{points}')
        break
    else: 
        print("ohh your missed it", "The Number is less than your guess" if a>b else "The Number is greater than your guess")
        points-=1
    if points <5 :
        print("OHh you ran out of Lives, pls try again")
        break
