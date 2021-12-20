def swap(s, _n):
    i = 0
    while i < _n - 1: # Проходим в цикле всю строку и сдвигаем девочек вперед
        if s[i] == "B" and s[i + 1] == "G": # Проверка стоит ли мальчик перед девочкой
            s = s[:i] + "G" + s[i+1:] # Так как строки неизменяемы, режем строку, прибавляем нужное значение, а потом оставшуюся часть строки
            s = s[:i+1] + "B" + s[i+2:]
            i = i + 2 # Если парочка поменялась местами, то пропускаем их обоих
        else:
            i = i + 1 # Иначе пропускаем одного
    return s # Возвращаем строку с парочками поменянными местами


if __name__ == '__main__':
    n, t = map(int, input().split())  # вводим данные через пробел, разбиваем функцией split и функцией map присваиваем им тип данных int
    queue = input()
    for i in range(t): # Раз в секунду вызываем функцию swap, которая проходит по строке и меняет местами детей
        queue = swap(queue, n)
    print(queue)
