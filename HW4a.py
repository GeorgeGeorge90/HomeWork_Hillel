
user_input = input("Будь ласка введіть строку зі слів: ")

splited_user_input = len(user_input.split())

consonant_list =['b', 'c', 'd', 'f', 'g','h','j','k',
                 'l','m','n','p','q','r','s','t','v','w','x','z']

countwords = ''
add_word = ''

for word in splited_user_input:
    counter = 0
    for letter in word:
        if letter in consonant_list:
            counter += 1
        if counter == 2:
            add_word = word
        if counter == 3:
            add_word = 0
            break
        if letter not in consonant_list:
            counter = 0
    if add_word == 0:
        break
    if len(add_word) > len(long_word):
        long_word = add_word
if add_word == 0:
    pass
else:
    print(f'The longest word with the couple consonants: {long_word}')

