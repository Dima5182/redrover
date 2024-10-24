class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

rect = Rectangle(2, 4)

a = rect.area()
p = rect.perimeter()

class Car:
    def __init__(self, make, max_speed):
        self.make = make
        self.max_speed = max_speed
        self.speed = 0

    def display_speed(self):
        print(self.speed)

    def accelerate(self):
        self.speed += 10
        if self.speed > self.max_speed:
            self.speed = self.max_speed

    def brake(self):
        self.speed -= 10
        if self.speed < 0:
            self.speed = 0

my_toyota = Car("Toyota", 180)
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.display_speed()

class BankAccount:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount
        if self._balance < 0:
            self._balance = 0
            print('Недостаточно средств!')

    def get_balance(self):
        return self._balance

account = BankAccount("Maria", 1000)
account.deposit(700)
account.withdraw(200)
print(account.get_balance())

class OverdraftAccount(BankAccount):
    def withdraw(self, amount):
        self._balance -= amount

jack_account = OverdraftAccount("Jack", 0)
jack_account.withdraw(100)
jack_account.withdraw(100)
jack_account.withdraw(100)
print(jack_account.get_balance())