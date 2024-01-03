try:
    with open('C:/Users/Pankaj Kumar/Desktop/CodePractice/27/hello.txt', 'r') as file:
        content = file.read()
        print("File contents:")
        print(content)

finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("file closed")
print(locals())