import csv



with open("C:/Users/Pankaj Kumar/Desktop/CodePractice/27/hello.csv", 'r', newline='') as csv_file:
    #creating a CSV reader object
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(', '.join(row))
        
        
    