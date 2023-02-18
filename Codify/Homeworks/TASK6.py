1 задание

Напишите функцию sum_range(start, end), которая суммирует все целые числа
от значения «start» до величины «end» включительно. Если пользователь задаст
первое число большее чем второе, просто поменяйте их местами.


def sum_range(start, end):
    
    try:
        if start > end:
            start, end == end, start
    except RecursionError:
        return False
    else:
        return sum(range(sum_range(start, end + 1))



2 задание

Написать функцию date, принимающую 3 аргумента — день, месяц и год.
Вернуть True, если такая дата есть в нашем календаре, и False иначе.


def date(day, month, year):
    import datetime
    try:
        datetime.date(year, month, day)
    except ValueError:
        return False
    else:
        return True
    
day = int(input('Введите день: '))
month = int(input('Введите месяц: '))
year = int(input('Введите год: '))

print(date(day, month, year))



3 задание

Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
и возвращающую True, если оно простое, и False - иначе.


def is_prime(number):
    if number % number == 0 and number != 0:
        return True
    else:
        return False
    
number = int(input('Введите число от 1 до 1000: '))
print(is_prime(number))



4 задание

Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3
значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.


def square(cube):
    p = 4*cube
    s = cube*cube
    d = (cube**2) / 2
    d = d**0.5
	
    k = (p, s, d)
	
    return k
	
print(square(16))



5 задание

Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True,
если год високосный, и False иначе.


def id_year_leap(year):
    
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


year = int(input('Введите год: '))
print(id_year_leap(year))



6 задание

Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция,
которая должна быть произведена над ними. Если третий аргумент +, сложить их; если —,
то вычесть; * — умножить; / — разделить (первое на второе).
В остальных случаях вернуть строку "Неизвестная операция".


def arithmetic(number_one, number_two, operation):
    
    if operation == '+':
        return (number_one + number_two)
    elif operation == '-':
        return (number_one - number_two)
    elif operation == '*':
        return (number_one * number_two)
    elif operation == '/':
        return (number_one / number_two)
    else:
        print('Неизвестная ошибка')


7 задание

Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых
(каждый год размер его вклада увеличивается на 10%.   Эти деньги прибавляются к сумме вклада, 
и на них в следующем году тоже будут проценты). Написать функцию bank, принимающая аргументы 
a и years, и возвращающую сумму, которая будет на счету пользователя.


def bank(a, years):
        for i in range(1,years+1):
                a += 0.1*a
        return a
print(bank(100, 5))