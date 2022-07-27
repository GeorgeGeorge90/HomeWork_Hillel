class Human:
    population = 0

    def __init__(self, name, surname, age, sex):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.__class__.population += 1

    def eat(self, dish):
        print(f"{self.name} eating {dish}")

    def sleep(self):
        print(f"{self.name} sleeps")

    def talk(self):
        print(f"{self.name} talking")

    def walk(self):
        print(f"{self.name} walking")

    def stand(self):
        print(f"{self.name} standing")

    def lie(self):
        print(f"{self.name} lying")


Neo = Human('Keanu', 'Reeves', '30', 'man')

Neo.walk()

Trinity = Human('CarrieAnne', 'Moss', '30', 'woman')

Trinity.stand()

Morpheus = Human('Laurence', 'Fishburn', '40', 'program')

Morpheus.talk()

print('Population: ', Human.population)


