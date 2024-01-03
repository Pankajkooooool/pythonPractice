with open("C:/Users/Pankaj Kumar/Desktop/CodePractice/fruits.txt.", 'r') as file:
    i =1 
    lines_with_numbers = [(f"{i+1}: {line.strip()}\n") for i, line in enumerate(file)]

with open("C:/Users/Pankaj Kumar/Desktop/CodePractice/27/NumberedFruit.txt.", 'w') as output_file:
    output_file.writelines(lines_with_numbers)