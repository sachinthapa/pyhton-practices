class Car:
    def __init__(self, color, milage):
        self.color = color;
        self.milage = milage;

    def __repr__(self):
        return '{self.__class__.__name__}({self.color},{self.milage})'.format(self=self)

    def __str__(self):
        return 'Car __str__'

my_car = Car('red','15')

print('{}'.format(my_car))
print(repr(my_car))
