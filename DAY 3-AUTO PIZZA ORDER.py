# An automatic pizza order
print('Hello!, here to take your order')
Size = input('What size of pizza do you want? S, M, or L\n')
Pepperoni = input('Do you want pepperoni? Y or N\n')
Extra_cheese = input('Do you want extra cheese? Y or N\n')

bill = 0
if Size == 'S':
    bill += 15
elif Size == 'M':
    bill += 20
elif Size == 'L':
    bill += 25

if Pepperoni == 'Y':
    if Size == 'S':
        bill += 2
    else:
        bill += 3

if Extra_cheese == 'Y':
    bill += 1


print('Your Total Bill is:' + ' ' + '$' + str(bill))
