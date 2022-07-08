
user_input = input("Будь ласка введіть аргумент: ")

def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        print("Число = ", val)
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            print("Число(float) = ", val)
        except ValueError:
            print("Це строка")

check_user_input(user_input)






