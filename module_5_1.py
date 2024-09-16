class House:
    def __init__(self, name, number_of_floors):
        self.name = name                          # Инициализируем атрибуты объекта
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:   # Проверка на допустимость этажа
            for floor in range(1, new_floor + 1):    # Вывод последовательности чисел от 1 до new_floor
                print(floor)
        else:
            print("Такого этажа не существует")    # Сообщение об ошибке

# Пример использования класса
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# Вызов метода go_to
h1.go_to(5)  # Вывод: 1, 2, 3, 4, 5
h2.go_to(10)  # Вывод: "Такого этажа не существует"