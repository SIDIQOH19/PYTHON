# To build a simple alculator that performs addition, multiplication, and division.

num1 = int(input('Input a number. '))
num2 = int(input('Input a second number. '))
operator = input('select an operator. ')

if operator == '+':
    print('The addition is:', num1 + num2)
elif operator == '-':
    print('The subtraction is:', num1 - num2)
elif operator == '*':
    print('The multiplication is:', num1 * num2)
elif operator == '/':
    print('The division is:', num1 / num2)
else:
    print('Operator is unavailable.')
