def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

print(add(2,3,4,5,6))

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw["make"] # required
        self.model = kw.get("model") # optional

my_car = Car(make="Cadillac")
print(my_car.make)