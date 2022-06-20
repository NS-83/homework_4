"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""


def increase_account():
    return sum_input('пополнения')


def make_purchase(account_sum):
    purchase_sum = sum_input('покупки')
    if purchase_sum > account_sum:
        print(f'На счету не хватает {purchase_sum - account_sum}!')
    else:
        purchase_name = input('Введите название покупки: ')
        return {'purchase_name': purchase_name, 'purchase_sum': purchase_sum}


def print_purchase_history(purchase_list):
    for purchase_data in purchase_list:
        print(f'Покупка: {purchase_data["purchase_name"]} Сумма: {purchase_data["purchase_sum"]}')



def sum_input(sum_type):
    while True:
        sum_string = input(f'Введите сумму {sum_type}: ').strip()
        if sum_string.isdigit():
            return int(sum_string)
        else:
            if sum_string.find(',') != -1:
                sum_string = sum_string.replace(',', '.')
            sum_string_parts = sum_string.split('.')
            sum_string_parts = list(filter(lambda x: x.isdigit(), sum_string_parts))
            if len(sum_string_parts) == 2:
                return float(sum_string)
        print('Введена некорректная сумма!')


account = 0
#Можно историю покупок сделать просто словарем, но хочется вывод по порядку
purchase_history = []
while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню')
    if choice == '1':
        account += increase_account()
    elif choice == '2':
        purchase = make_purchase(account)
        if purchase:
            account -= purchase['purchase_sum']
            purchase_history.append(purchase)
    elif choice == '3':
        print_purchase_history(purchase_history)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')