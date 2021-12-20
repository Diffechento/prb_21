def possibility(list_, destination):
    location = list_[0]     # Перемещаем человека по первому порталу
    while location < destination: # Пока местонахождение не достигнет пункта назначения перемещаемся по порталам по порядку
        location += list_[location - 1]
    if location == destination: # Проверяем попали ли в пункт назначения
        return ("YES")
    else:
        return ("NO")

if __name__ == '__main__':
    n, t = map(int, input().split()) # вводим данные через пробел, разбиваем функцией split и функцией map присваиваем им тип данных int
    portals = map(int, input().split(" "))
    print(possibility(list(portals), t))
