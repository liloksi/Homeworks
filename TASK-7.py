# Программа авиарейсов

flights = [
    {'number': 1, 'name': 'Бишкек-Москва', 'time': '15:00', 'price': 20000},
    {'number': 2, 'name': 'Бишкек-Ош', 'time': '03:00', 'price': 5000},
    {'number': 3, 'name': 'Бишкек-Стамбул', 'time': '23:00', 'price': 40000},
    {'number': 4, 'name': 'Стамбул-Берлин', 'time': '05:00', 'price': 25000},
    {'number': 5, 'name': 'Нью-Йорк-Бишкек', 'time': '07:00', 'price': 130000},
]

print('\nСегодняшние авиарейсы:\n')


for flight in flights:
    print(f'Номер: {flight["number"]} | Авиарейс: {flight["name"]} | Время: {flight["time"]} | Цена: {flight["price"]}')


flight_info = None

print('\nВыберите авиарейс')


while True:
    try:
        flight_number = int(input('\nВведите номер авиарейса: '))
        if flight_number > len(flights):
            print('Авиарейс не выбран. Вы ввели число больше 5')


    except ValueError:
        print('Авиарейс не выбран. Вы ввели не номер, пожалуйста введите номер авиарейса!')
        continue

    else:
        username = input('Введите свое имя: ')
        flight_info = flights[flight_number - 1]
        print(f'Авиарейс выбран. Вы {username.title()} выбрали авиарейс: {flight_number}')
    break


while True:
    try:
        ticket_price = int(input('\nВведите сумму билета: '))

    except ValueError:
        print('Введена неверная сумма. Пожалуйста, введите действительную сумму за билет!')
        continue

    else:
        if ticket_price < flight_info['price']:
            print(f'Ошибка: Введенная вами сумма {ticket_price} меньше, чем стоимость билета на {flight_info["price"]}')
        else:
            change = ticket_price - flight_info['price']
            print(f'Ваш билет на рейс куплен {flight_info["name"]}')
            print(f'Сдача: {change}')
    break


print('\nВы купили билет: ')
print(f'Номер: {flight["number"]} | Авиарейс: {flight["name"]} | Время: {flight["time"]} | Цена: {flight["price"]}')