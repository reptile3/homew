"""
Создать новый класс Cat, который имеет все те же атрибуты что и Dog,
только заменить метод bark на meow.
"""


class Cat:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print(f"Jump {self.name}")

    def run(self):
        print(f"Run {self.name}")

    def meow(self):
        print(f"Meow {self.name}")

    def change_name(self, name):
        self.name = name


if __name__ == "__main__":
    cat_bob = Cat(100, 100, "Bob", 10)
    cat_bob.meow()
    cat_bob.change_name("William")
    cat_bob.change_name("Bob")

    print(cat_bob.name)
    print(cat_bob.height)
    print(cat_bob.weight)
    print(cat_bob.age)