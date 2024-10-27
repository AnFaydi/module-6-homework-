# 2 класса родителя: Animal, Plant
# Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное название каждого животного.

#
# 4 класса наследника:
# Mammal, Predator для Animal.
# Flower, Fruit для Plant.
#
# У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
# eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.
#
# Метод eat должен работать следующим образом:
# Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>", меняется атрибут fed на True.
# Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>", меняется атрибут alive на False.
# Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.
#
# У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)
#
# Создайте объекты классов и проделайте действия затронутые в примере результата работы программы.

# Помните, обращаясь к атрибутам объекта текущего класса используйте параметр self.
# Передавая объекты классов Fruit и Flower в метод eat, так же можно обращаться к их атрибутам внутри.
# Обращайте внимание на то, где атрибут класса, а где атрибут объекта.
class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def eat(self, food): #где food - это параметр, принимающий объекты классов растений.
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            Animal.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            Animal.alive = False
class Predator(Animal):
    def eat(self, food): #где food - это параметр, принимающий объекты классов растений.
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            Animal.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            Animal.alive = False
class Plant:
    edible = False
    def __init__(self, name):
        self.name = name
    # Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения

class Flower(Plant):
    pass
class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.

# У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)
#
# Создайте объекты классов и проделайте действия затронутые в примере результата работы программы.

# Помните, обращаясь к атрибутам объекта текущего класса используйте параметр self.
# Передавая объекты классов Fruit и Flower в метод eat, так же можно обращаться к их атрибутам внутри.
# Обращайте внимание на то, где атрибут класса, а где атрибут объекта.