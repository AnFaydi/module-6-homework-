class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.owner = owner
        self._model = model
        self._engine_power = engine_power
        self._color = color
    def get_model(self):
        return f"Модель: {self._model}"
    def get_horsepower(self):
        return f"Мощность двигателя: {self._engine_power}"
    def get_color(self):
        return f"Цвет: {self._color}"
    def print_info(self):
        return (f'{Vehicle.get_model(self)}\n{Vehicle.get_horsepower(self)}'
                f'\n{Vehicle.get_color(self)}\nВладелец: {self.owner}')
    def set_color(self, new_color: str):
        for colors in self.__COLOR_VARIANTS:
            if new_color.upper() == colors.upper():
                self._color = new_color
                return
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
print(vehicle1.print_info())
vehicle1.get_model()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
print(vehicle1.print_info())