
upper_limit = float(input("Будь ласка введіть максимальну ціну: "))

lower_limit = float(input("Будь ласка введіть мінімальну ціну: "))


catalog = { "cilpio": 47.999,
            "a_studio": 42.999,
            "momo": 49.999,
            "main-service": 37.245,
            "buy.ua": 38.324,
            "my-store": 37.166,
            "the_partner": 38.988,
            "sto": 37.720,
            "rozetka": 38.003,
            }


for key, value in catalog.items():
    if lower_limit < value < upper_limit:
        print('Магазин який вас влаштує: ',key)
    elif value < lower_limit:
        print('Нажаль у списку немає магазина, який вас влаштує')
