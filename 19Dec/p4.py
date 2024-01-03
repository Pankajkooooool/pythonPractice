st = "Hello 123 World 456!"
lt= []

for s in st:
    if s.isdigit():
        lt.append(int(s))
print(lt)