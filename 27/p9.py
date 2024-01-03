


with open("C:/Users/Pankaj Kumar/Desktop/CodePractice/27/NumberedFruit.txt.", 'r') as file:
 
    lines = [line.strip() for line in file]
    reversed_lines = reversed(lines)

with open("C:/Users/Pankaj Kumar/Desktop/CodePractice/27/NumberedFruit.txt.", 'w') as file:
    file.write('\n'.join(reversed_lines))
