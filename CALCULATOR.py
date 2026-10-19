# Basic Calculator program
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    continue_calculating = True

    num1 = float(input('Enter your first number: '))

    while continue_calculating:
        for symbol in operations:
            print(symbol)
        operation_symbol = input('Pick an operator: ')
        num2 = float(input('Enter the second number: '))
        result = operations[operation_symbol](num1, num2)
        print(f'{num1} {operation_symbol} {num2} = {result}')
        user_input = input(
            f"Type 'y' to continue calculating with {result} or 'n' to restart\n").lower()
        if user_input == 'y':
            num1 = result
        else:
            continue_calculating = False
            print('\n' * 10)
            calculator()


calculator()
