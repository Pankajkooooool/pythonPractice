adjectives = ["Happy", "Terrific", "Wonderful", "Thrilling", "Fantastic", "Super", "Relaxing"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

favD = input("Enter your fav Day: ")
index = days.index(favD)
print(f"{adjectives[index]}-{favD}")
