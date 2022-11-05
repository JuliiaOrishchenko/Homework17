class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("woof woof")


class Cat(Animal):
    def talk(self):
        print("meow")


def choose():
    user_chose = input("Choose animal: ")
    if user_chose.lower() == "cat":
        instance = Cat()
    elif user_chose.lower() == "dog":
        instance = Dog()
    instance.talk()


choose()



