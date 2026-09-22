# To calculate bill per person using tip
print('This is a Tip Calculator')
bill = float(input('What is your Total bill?\n'))
tip = int(input('What percentage tip wpould you like to give? 10 12 15\n'))
people = int(input('How many people are paying for the tip?\n'))
tip_per_person = (bill/people) * tip
print('Each person will pay:' + ' ' + str(tip_per_person))
