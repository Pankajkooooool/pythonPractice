def findfreq(input_str) :
    charfreq = {}
    for char in input_str:
        charfreq[char] = charfreq.get(char,0) + 1 
    
    # maxi = max(charfreq.values() )
    maxi = max(charfreq, key=charfreq.get)
    print(f"{maxi}, {charfreq[maxi]}")

findfreq("Pankaj is the greatest ttt   aaaaaaaaaaaaa")