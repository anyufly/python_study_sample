class Duck:
    def __init__(self, name, foot_number):
        self.name = name
        self.foot_number = foot_number

    def say(self):
        print('I\'m a duck!,My name is ' + self.name + ' ~GaGaGa！')

    def go(self):
        print('Walking on ' + self.foot_number + ' feet' + ' ~GaGaGa!')


class Dog:
    def __init__(self, name, foot_number):
        self.name = name
        self.foot_number = foot_number

    def say(self):
        print('I\'m a dog!,My name is ' + self.name + ' ~WangWangWang！')

    def go(self):
        print('Walking on ' + self.foot_number + ' feet' + ' ~WangWangWang!')


class Cat:
    def __init__(self, name, foot_number):
        self.name = name
        self.foot_number = foot_number

    def say(self):
        print('I\'m a cat!,My name is ' + self.name + ' ~MiuMiuMiu！')

    def go(self):
        print('Walking on ' + self.foot_number + ' feet' + ' ~MiuMiuMiu')


def talk_and_walk(target_animal):
    # 只要实现了say()方法和go()方法就是动物,而不需要继承于某个积累
    target_animal.say()
    target_animal.go()


duck = Duck('Town', 'two')
dog = Dog('Tom', 'four')
cat = Cat('Kitty', 'four')

animals = [duck, dog, cat]

for animal in animals:
    talk_and_walk(animal)
