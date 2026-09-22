student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

for key, value in student_scores.items():
    if value >= 91 and value <= 100:
        print('Outsatnding')
    print(key, value)
