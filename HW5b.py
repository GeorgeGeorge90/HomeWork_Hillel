
def get_float():
    value = None

    while value is None:
        try:
            value = float(input(f'Введіть цифрове значення: '))
        except:
            print (float(0))

    return value

user_number = get_float()

print('=====>', user_number)