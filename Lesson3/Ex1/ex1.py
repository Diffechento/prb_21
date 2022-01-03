import math
# Функция возвращает долготу и широту из строки
def find_coord(coord):
    if len(coord) != 80: # Проверяем не битая ли строка
        return 1
    else:
        coord = coord.split(",")
        return float(coord[2]), float(coord[4])

# Функция возвращает время из строки
def find_time(time):
    time = time.split(",")
    h = time[1][0:2]
    m = time[1][2:4]
    s = time[1][4:6]
    ms = time[1][6:]
    return str(h + ":" + m + ":" + s + ms)

# Функция конвертирует формат координат nmea в десятичный
def convert(data):
    deg1 = math.trunc(data[0] / 100)
    coord1 = deg1 + (data[0] - 100 * deg1) / 60
    deg2 = math.trunc(data[1] / 100)
    coord2 = deg2 + (data[1] - 100 * deg2) / 60
    coord = coord1, coord2
    return coord

# Функция находит расстояние между точками
def dist(a, b):
    phi1 = math.radians(a[0])
    lam1 = math.radians(a[1])
    phi2 = math.radians(b[0])
    lam2 = math.radians(b[1])
    dphi = phi2 - phi1
    dlam = lam2 - lam1
    delta = 2 * math.asin(
        math.sqrt(math.pow(math.sin(dphi / 2), 2) + math.cos(phi1) * math.cos(phi2) * math.pow(math.sin(dlam / 2), 2)))
    distance = 6372795 * delta
    return distance

# Функция поиска подходящих промежутков
def searchtime():
    flag = False
    f = open('nmea.log')
    i = 0
    point = (60.051584, 30.300509)
    for line in f:
        if find_coord(line) != 1:
            location = convert(find_coord(line))
            if dist(location, point) < 25 and flag is True:
                time2 = find_time(line)
            elif dist(location, point) < 25:
                time1 = find_time(line)
                flag = True
            elif dist(location, point) > 25 and flag is True:
                print("Расстояние до заданной точки было 25м в промежутке от ", time1, "до ", time2)
                flag = False


if __name__ == '__main__':
    searchtime()
