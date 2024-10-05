class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return int(self.number_of_floors)

    def __str__(self):
        return str(f'Название: {self.name}, кличество этажей: {self.number_of_floors}')


    def go_to(self, new_floor):
        for i in range(1, int(new_floor + 1)):
            if new_floor > self.number_of_floors or new_floor == 0:
                print('Такого этажа не существует')
                break
            else:
                print(i)

#house_love = House('Пятиэтажка', 5)
#house_love.go_to(5)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))