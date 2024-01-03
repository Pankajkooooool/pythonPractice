while True:
    try:
        user_input = input("Enter a number: ")
        number = float(user_input)
        result = 10 / number

        print(f"10 divided by {number} is {result}")
        break

    except ValueError:
        print("Please enter a valid number.")

    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a non-zero number.")

    except Exception as e:
        print(f"An error occurred: {e}")