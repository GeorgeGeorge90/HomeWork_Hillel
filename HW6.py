
age = int(input("Будь ласка введіть свій вік: "))


def declination(age):
    """
        Returns declination for given age:

                Parameters:
                        age (int): age of the cinema visitor

                Returns:
                        declination (str): declination for given age
    """
    if (age % 10 == 1) and (age != 11) and (age != 111):
        return "рік"
    elif (age % 10 > 1) and (age % 10 < 5) and (age != 12) and (age != 13) and (age != 14):
        return "роки"
    else:
        return "років"


def kasyr(age):
    """
            Forming string within age and declination for print

                    Parameters:
                            age (int): age of the cinema visitor

    """
    dec = declination(age)
    if age < 7:
        print(f"Тобі ж {age} {dec}! Де твої батьки?")
    elif age // 10 == age % 10:  # finding repdigit
        print(f"О, вам {age} {dec}! Який цікавий вік!")
    elif age < 16:
        print(f"Вам {age} {dec}! Це фільм для дорослих!")
    elif age <= 65:
        print("А білетів вже немає!")
    elif age > 65:
        print(f"Вам {age} {dec}? Покажіть пенсійне посвідчення!")


kasyr(age)