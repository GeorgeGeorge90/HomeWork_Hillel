
user_input = input("Будь ласка введіть строку зі слів: ")

result = user_input.split()

consonant_list =['a', 'e', 'i', 'o', 'u', 'y']

word_count = 0

for word in result:
    counter = 0

    for letter in word:
        if letter in consonant_list:
            counter += 1
        else:
            counter = 0

        if counter == 2:
            word_count += 1
            break



print("У вашому реченні " + str(word_count) + " слів(слова) з голосними буквами підряд.")

