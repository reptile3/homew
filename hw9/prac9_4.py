"""
Создать общий класс Animal, содержащий все общие методы классов Dog и Cat.
Унаследовать Dog и Cat от класса Animal и Удалить в дочерних классах те методы,
которые имеются у родительского класса. Создать объект каждого класса и вызвать все его методы.
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def jump(self):
        print(f"Jump {self.name}")

    def run(self):
        print(f"Run {self.name}")

    def change_name(self, name):
        self.name = name
        print(f"New name is {self.name}")

class Cat(Animal):

    def meow(self):
        print(f"Meaw {self.name}")


class Dog(Animal):

    def bark(self):
        print(f"Bark {self.name}")

if __name__ == "__main__":
    my_animal = Animal("Catodog")
    my_animal.jump()
    my_animal.run()
    my_animal.change_name("dogocat")


    my_cat = Cat("kitty")
    my_cat.meow()


    my_dog = Dog("sweety")
    my_dog.bark()





