while True:
    try:
        user_input = input("Enter a word: ")

        if any(char.isdigit() for char in user_input):
            raise TypeError("Input must be a word, not a number.")

        if len(user_input) > 50:
            raise ValueError("Word is too long. Maximum length is 50 characters.")

        print(f"You entered: {user_input}")
        break

    except TypeError as te:
        print(f"Error: {te}")

    except ValueError as ve:
        print(f"Error: {ve}")