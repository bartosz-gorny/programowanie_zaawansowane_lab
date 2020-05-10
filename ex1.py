''' 
Zadanie 1: napisać klasę losującą 6 liczb, klasa ma zwracać 6 losow

- losujemy 6 cyfr ze wzrou
- za pomoca wywolania instancji klasy wypisujemy 6 liczb na ekranie
'''
import random

class Numbers:
    def __init__(self, name, count):
        self.name = name
        self.count = count
        numbers = random.sample(range(1,100), count)
        print (f"Generated {count} numbers: {numbers}")


losowanie1 = Numbers('losowanie1', 6)
losowanie2 = Numbers('losowanie2', 8)

