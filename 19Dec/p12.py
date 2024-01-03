
my_list = [1, 4, 7, 10, 15, 20, 'apple', 'banana', 'orange', 'kiwi']

for item in my_list[:]:
    if isinstance(item, int) and item % 2 == 0:
        my_list.remove(item)

for item in my_list[:]:
    if isinstance(item, str) and len(item) < 5:
        my_list.remove(item)

print("Modified List:", my_list)
