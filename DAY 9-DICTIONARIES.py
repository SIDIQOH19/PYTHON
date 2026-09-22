# To create dictionaries in python
unilag = {
    'faculty': ('engineeering', 'masscom', 'science', 'education'),
    'departments': ('computer engineering', 'botany', 'insurance', 'law', 'economics'),
    'levels': ('100', '200', '300', '400', '500')
}

unilag['class'] = 'social sciences'
del unilag['class']

for keys, values in unilag.items():
    print(keys, values)


# Nested list and distionaries
