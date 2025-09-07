def add_two_numbers(num1, num2):
    """ Adds two numbers and returns the sum. """
    return num1 + num2

def main():
    # Take user's input
    try:
        print("Add Two Numbers")
        input1 = float(input("Enter first number: "))
        input2 = float(input("Enter second number: "))
    except:
        print("Invalid input. Please run again and enter numeric values.")
        return

    # Call the function to add two numbers
    result = add_two_numbers(input1, input2)
    print(f"The sum of {input1} and {input2} is: {result}")

if __name__ == "__main__":
    main()