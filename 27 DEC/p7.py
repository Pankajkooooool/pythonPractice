# Start with any positive integer n.
# If n is even, divide it by 2.
# If n is odd, multiply it by 3 and add 1.
# Repeat the process until n reaches 1.

n = 69
while n != 1:
    if n%2 == 0:
        n = n/2
    else :
        n = n*3+1
        
print(n)
