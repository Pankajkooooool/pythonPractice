def findDub(input_str) :
    charfreq = {}
    for char in input_str:
        charfreq[char] = charfreq.get(char,0) + 1 
    
    for key, value in charfreq.items():
        if value > 1:
            print(f"'{key}' appears {value} times")

findDub("Pankaj")
