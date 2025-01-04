from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    done = False
    number1 = float(input("What's the first number?: "))

    while not done:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        number2 = float(input("What's the next number?: "))
        result = operations[operation_symbol](number1, number2)
        print(f"{number1} {operation_symbol} {number2} = {result}")
        calculate_again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if calculate_again == 'y':
            number1 = result
        elif calculate_again == 'n':
            done = True
            print("\n" * 20)
            calculator()


calculator()
