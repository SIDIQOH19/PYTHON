sentence = input('Enter your sentence: ')
print('Your Sentence is:', sentence)

word_to_remove = input('What word do you want to replace? ')

new_word = input('What is the word you want to replace it with? ')

print(sentence.replace(word_to_remove, new_word))
