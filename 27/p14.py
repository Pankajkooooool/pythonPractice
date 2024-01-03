
def Openfile(file_path):
    try:
        with open(file_path, 'r') as file:
            print(f"File '{file_path}' successfully opened.")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

    except PermissionError:
        print(f"Error: Permission denied while trying to open '{file_path}'.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

file_path = 'hello.txt' 
Openfile(file_path)