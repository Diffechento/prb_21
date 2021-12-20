def string_lenght(string):
    return (len(set(string)))  # С помощью функции set удаляем из строки повторяющиеся символы,функцией len получаем длину полученной строки и возвращаем значение


if __name__ == '__main__':
    input_string = input()  # Вводим строку с клавиатуры
    print(string_lenght(input_string)) # Выводим значение функции

