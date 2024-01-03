string = "A new Fox jumps in the grapevine and That is a problem for the farmeers"
lt = {}
string = string.lower()
for char in string:
    if char.isalpha():
        lt[char] = lt.get(char,0) + 1
        
Max = max(lt,key=lt.get)     
print(f"the most common character here is '{Max}', appearing {string.count(Max)} times")
