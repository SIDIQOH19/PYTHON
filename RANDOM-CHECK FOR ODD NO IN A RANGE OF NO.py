count = 0
for number in range(1, 100):
    if number % 2 == 1:
        count += 1
        print(number)
print(f'There are {count} odd numbers between 1 and 100')
