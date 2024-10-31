from math import pi, sqrt
class Figure:
    sides_count = 0
    def __init__(self, color, sides):
        color = list(color)
        self.__sides = sides
        self.__color = color
        self.filled = bool()
    def get_color(self):
        return self.__color
    def __is_valid_color(self, r, g, b):
        if (isinstance(r, int) and r >= 0 and r <= 255 and isinstance(g, int) and g >= 0 and
                g <= 255 and isinstance(b, int) and b >= 0 and b <= 255):
            return True
        else:
            return False
    def set_color(self, r, g, b):
        if Figure.__is_valid_color(self, r, g, b) == True:
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b
    def __is_valid_sides(self, args):
        if len(args) == self.sides_count:
            for i in args:
                if isinstance(i, int) and i > 0:
                    is_true = True
                else:
                    is_true = False
                if is_true == False:
                    return False
            return True
        else:
            return False
    def get_sides(self):
        return self.__sides
    def __len__(self):
        return sum(self.__sides)
    def set_sides(self, *new_sides):
        new_sides = list(new_sides)
        if Figure.__is_valid_sides(self, new_sides):
                self.__sides = new_sides
class Circle(Figure):
    sides_count = 1
    def __init__(self, color: tuple, *sides):
        sides = list(sides)
        if len(sides) != self.sides_count:
            sides = [1]
        super().__init__(color, sides)
        self.__radius = sides[0] / (2*pi)
    def get_square(self):
        return pi*(self.__radius**2)
class Triangle(Figure):
    sides_count = 3
    def __init__(self, color: tuple, *sides):
        sides = list(sides)
        if len(sides) == 1:
            sides = [sides[0], sides[0], sides[0]]
        if len(sides) == 2 or len(sides) > 3:
            sides = [1, 1, 1]
        super().__init__(color, sides)

    def get_square(self):
        side = super().get_sides()
        p = sum(side)/2
        return sqrt(p * (p - side[0]) * (p - side[1]) * (p - side[2]))

class Cube(Figure):
    sides_count = 12
    def __init__(self, color: tuple, *sides):
        sides = list(sides)
        if len(sides) == 1:
            sides = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if len(sides) > 1 and len(sides) < 12:
            for i in range(self.sides_count):
                sides[i] = 1
        super().__init__(color, sides)
    def get_volume(self):
        side = super().get_sides()
        return side[0]**3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
