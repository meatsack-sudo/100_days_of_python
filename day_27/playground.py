def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)

add(1, 2, 3, 4, 5)

def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiple"]
    print(n)


calculate(3, add=3, multiple=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.seatcolor = kw.get("car_color")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)