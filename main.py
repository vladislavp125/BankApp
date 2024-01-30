balance = 0
year = 2024
transactions_data = {}
user_data = {}
user_balance = {}
limite_d = {}
password = ''


def recover_data_YES():
    with open('data_transaction.txt', encoding='UTF-8') as file_data_transaction:
        for line in file_data_transaction:
            if line == '\n':
                continue
            else:
                comment, expected_amount = line.split()
                transactions_data[comment] = expected_amount
    with open('user_data.txt', encoding='UTF-8') as file_user_data:
        for line in file_user_data:
            if line == '\n':
                continue
            else:
                key, value = line.split()
                user_data[key] = value
    with open('user_balance.txt', encoding='UTF-8') as file_user_balance:
        for line in file_user_balance:
            key, value = line.split()
            user_balance[key] = value
    with open('limit_data.txt', encoding='UTF-8') as file:
        for line in file:
            if line != '':
                key, value = line.split()
                limite_d[key] = value
            else:
                continue
    name = user_data['name']
    age = user_data['age']
    user_data['balance'] = user_balance['balance']
    user_data['limite'] = limite_d['limite']

    print('С возвращением ' + name + ' !')
    print('Ваш баланс: ' + str(user_data['balance']))
    return user_data


def recover_data_NO():
    with open('data_transaction.txt', 'w', encoding='UTF-8') as file_data_transaction:
        file_data_transaction.write('')
    with open('user_data.txt', 'w', encoding='UTF-8') as file_user_data:
        file_user_data.write('')
    with open('user_balance.txt', 'w', encoding='UTF-8') as file_user_balance:
        file_user_balance.write('')
    with open('limit_data.txt', 'w', encoding='UTF-8') as file:
        file.write('')


def operation_user():
    print('-----------------Банковское приложение-----------------')
    print('Меню:')
    print('1.Создать аккаунт')
    print('2.Положить деньги на счет')
    print('3.Снять деньги')
    print('4.Вывести баланс на экран')
    print('5.Выставление ожидаемого пополнения')
    print('6.Установить максимальный лимит')
    print('7.Выполнить запланированные транзакции')
    print('8.Статистика по ожидаемым пополнениям')
    print('9.Фильтрация отложенных пополнений')
    print('10.Выйти из программы')
    operation_in = int(input('Введите номер операции: '))
    return operation_in


def create_user():
    try:
        name = input('Введите ФИО: ')
        age = int(input('Введите год рождения: '))
        print('Создан аккаунт: ' + name + ' (' + str(year - age) + ' лет)')
        password = input('Придумайте пароль: ')
        print('Аккаунт успешно зарегистрирован!')
        with open('user_data.txt', 'w', encoding='UTF-8') as file:
            file.write('name ' + str(name) + '\n' + 'age ' + str(age) + '\n' + 'password ' + str(password))
        return password
    except ValueError:
        print()
        print('Год рождения должен состоять только из цифр !!')
        print()



def money_up(balance):
    try:
        cash_up = int(input('Введите сумму пополнения: '))
        print('Счет успешно пополнен!')
        balance += cash_up
        with open('user_balance.txt', 'w', encoding='UTF-8') as file_user_balance:
            file_user_balance.write('balance ' + str(balance))
        return balance
    except ValueError:
        print()
        print('Чтобы пополнить баланс введите верную сумму, возможно вы пытаетесь ввести слово!')
        print()


def money_to_cash(balance, password):
    try:
        user_password = input('Введите пароль: ')
        if password == user_password:
            cash_down = int(input('Ваш баланс: ' + str(balance) + 'руб. Введите сумму для снятия: '))
            if cash_down > balance:
                print('Недостаточно средств для снятия.')
            elif cash_down <= 0:
                print('Сумма указана некорректно, попробуйте ещё раз! ')
            else:
                balance -= cash_down
                print('Снятие успешно завершено, ваш баланс: ' + str(balance))
        else:
            print('Неверный пароль! Попробуйте ещё раз.')

        with open('user_balance.txt', 'w', encoding='UTF-8') as file_user_balance:
            file_user_balance.write('balance ' + str(balance))
        return balance
    except ValueError:
        print()
        print('Чтобы снять денежные средства, необходимо указать верную сумму, возможно вы пытаетесь ввести слово!')
        print()


def check_balance(balance, password):
    try:
        user_password = str(input('Введите пароль: '))
        if password == user_password:
            print('Ваш баланс: ' + str(balance))
        else:
                print('Неверный пароль! Попробуйте ещё раз.')
    except:
        print('Непредвиденная ошибка!')
        print()


def transaction(transactions):
    try:
        expected_amount = int(input('Введите сумму ожидаемого пополнения: '))
        comment = str(input('Уточните пожалуйста назначение пополнения: '))
        transactions_data[comment] = expected_amount
        count_tran = len(transactions)
        print('Ожидается ' + str(count_tran) + ' операций(я)')
        string_for_copy = ''
        with open('data_transaction.txt', encoding='UTF=8') as file_transaction:
            for line in file_transaction:
                string_for_copy += line
        with open('data_transaction.txt', 'w', encoding='UTF=8') as file_transaction:
            file_transaction.write(string_for_copy + '\n' + str(comment) + ' ' + str(expected_amount))
        return count_tran
    except ValueError:
        print()
        print('Вы вводите буквы, нужно ввести число!! ')
        print()

def max_limite():
    try:
        limite = int(input('Введите максимально допустимую сумму которая должна быть на счету: '))
        with open('limit_data.txt', 'w', encoding='UTF-8') as file:
            file.write('limite ' + str(limite))
        return limite
    except ValueError:
        print()
        print('Вы вводите буквы, нужно ввести число!! ')
        print()


def ran_transactions(transactions_data, limite):
    summ = 0
    try:
        for comment, expected_amount in list(transactions_data.items()):
            if int(expected_amount) < limite:
                summ += int(expected_amount)
                print('Транзакция "' + comment + '" на сумму ' + str(expected_amount) + 'руб. успешно применена.')
                del transactions_data[comment]
            else:
                print('Транзакция "' + comment + '" на сумму ' + str(expected_amount) + 'руб. не может быть применена('
                                                                                        'превышен лимит).')

        with open('data_transaction.txt', 'w', encoding='UTF=8') as file_transaction:
            for comment, expected_amount in list(transactions_data.items()):
                file_transaction.write(str(comment) + ' ' + str(expected_amount) + '\n')
        return summ
    except:
        print('Непредвиденная ошибка!')


def stat_expected_amount(transactions_data):
    rub = {}
    try:
        for comment, expected_amount in transactions_data.items():
            if expected_amount in rub:
                rub[expected_amount] += 1
            else:
                rub[expected_amount] = 1
        if rub != {}:
            for summ, num_payments in rub.items():
                print(str(summ) + ' руб: ' + str(num_payments) + ' платеж(а)')
        else:
            print('Нет запланированных операций! ')
    except:
        print('Непредвиденная ошибка!')


def filter_transaction_sub(transactions_data):
    for key, value in transactions_data.items():
        yield key, value


def filter_transaction():
    print()
    print('Данная операция выведет все отложенные пополнения которые больше введенного числа.')
    print()
    threshold = int(input('Введите число от которого будем проверять сумму транзакций: '))
    for transactions in filter_transaction_sub(transactions_data):
        if int(transactions[1]) >= threshold:
            print(f'Транзакция больше {threshold} рублей.: {transactions[0]}  {transactions[1]}')


def recover_data(password, balance):
    a = input('Уточните пожалуйста, нужно ли восстановить данные из файла? Y/N: ')

    try:
        if a == 'Y':
            recover_data_YES()
            password = user_data['password']
            balance = int(user_data['balance'])
            limite = int(user_data['limite'])
            return password, balance, limite
        else:
            recover_data_NO()
            return 0, 0, 0

    except FileNotFoundError:
        print()
        print('Не найден файл для восстановления! ')
        print()
        print('Сначала нужно создать аккаунт! ')
        exit()

    except:
        print()
        print('Возможно какой-то файл пустой или не может быть восстановлен! ')
        print()
        exit()


if __name__ == "__main__":
    password, balance, limite = recover_data(password, balance)
    while True:
        try:
            operation = operation_user()

            if operation == 1:
                    password = create_user()

            elif operation == 2:
                balance = money_up(balance)
                print()

            elif operation == 3:
                balance = money_to_cash(balance, password)
                print()

            elif operation == 4:
                check_balance(balance, password)
                print()

            elif operation == 5:
                transaction(transactions_data)
                print()

            elif operation == 6:
                limite = max_limite()
                print()

            elif operation == 7:
                balance += ran_transactions(transactions_data, limite)
                with open('user_balance.txt', 'w', encoding='UTF=8') as file_user_balance:
                    file_user_balance.write('balance ' + str(balance))
                print()

            elif operation == 8:
                stat_expected_amount(transactions_data)
                print()

            elif operation == 9:
                filter_transaction()
                print()

            elif operation == 10:
                print('Спасибо за пользование нашей программой, до свидания!')
                break
            else:
                print('Некорректный номер операции, попробуйте снова :(')
        except:
            print("Номер операции нужно указывать цифрами")
