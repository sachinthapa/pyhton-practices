import math

class Pizza:
    def __init__(self, ingridients):
        self.ingridients =  ingridients

    def __repr__(self):
       return f"{self.__class__.__name__}({self.ingridients!r})"

    @classmethod
    def margherita(cls):
        print(cls.dummy()
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

    @staticmethod
    def area(r):
        return r ** 2 * math.pi

    def dummy():
        return "I am dummy"


pizza = Pizza(['peporoni','pepper'])

print(pizza)
print(Pizza.prosciutto())
print(Pizza.margherita())
print(Pizza.area(4))
