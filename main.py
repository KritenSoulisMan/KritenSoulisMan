import psycopg2

def m_menu(credentials):
    login, password = credentials
    print('1. Изменить свой логин.\n'
          '2. Изменить свой пароль.\n'
          '3. Калькулятор.\n'
          '4. Завершить сессию.')
    a = int(input('Введите номер пункта: '))

    if a == 1: # Смена логина.
        login = input('Логин: ')
        print('Логин успешно изменён.')
        return [login, password]

    elif a == 2: # Смена пароля.
        password = input('Пароль: ')
        print('Пароль успешно изменён.')
        return [login, password]

    elif a == 3:
        print('ДОБРО ПОЖАЛОВАТЬ В КАЛЬКУЛЯТОР.\n'
              '1. Поиск кратных n.\n'
              '2. Умножение.\n'
              '3. Деление.\n'
              '4. Сумма.\n'
              '5. Разность.\n'
              '6. Степень.')
        b = int(input('Введите номер пункта: '))

        if b == 1: # Поиск чисел кратные n.
            print(f'Напишите несколько чисел. (через пробел) ')
            numbers = list(map(int, input('Ваши числа: ').split()))
            for nums in range(len(numbers)):
                n = int(input('Кратное: '))
                if nums % n == 0:
                    print(nums)
                    return

        if b == 2:
            x = int(input('1-е число: '))
            y = int(input('2-е число: '))
            sume_u = x * y
            print(sume_u)
            return

        if b == 3:
            x = int(input('1-е число: '))
            y = int(input('2-е число: '))
            sume_d = x / y
            print(sume_d)
            return

        if b == 4:
            x = int(input('1-е число: '))
            y = int(input('2-е число: '))
            sum = x + y
            print(sum)
            return

        if b == 5:
            x = int(input('1-е число: '))
            y = int(input('2-е число: '))
            minus = x - y
            print(minus)
            return

        if b == 6:
            x = int(input('Число: '))
            y = int(input('Степень числа: '))
            s = x ** y
            print(s)
            return

    elif a == 4: # Завершение программы
        return exit()

    else: # Если пользователь введёт отсутствующий вариант.
        print('Неверное значение.')
        return

def entry_acc(login, password):
    login = input('Логин: ')
    password = input('Пароль: ')
    credentials = [login, password]
    ls = {'0123456789$,%.!@#$^&*()_+=-?|/.,<>`~'}
    if not(any((c in ls) for c in password)) and len(password) < 8:
        print('Ваш пароль должен быть длинной 8 символов.\n'
              'Ваш пароль должен содержать 1 специальный символ.')
        return entry_acc(0, 0)
    else:
        print("Подключение...")
        cur = conn.cursor()
        # Вставка данных в таблицу users
        try:
            cur.execute("""INSERT INTO users (login, password) VALUES (%s, %s)""", (login, password))
            conn.commit()
            print("Успешная регистрация!")
            # Закрытие курсора и соединения
            cur.close()
            conn.close()
            return credentials
        except psycopg2.Error as e:
            print(f'Ошибка при подключении к базе данных: {e}')
            # print('Временно отсутствует подключение...')
            conn.rollback()
            return exit()

def auth_acc(login, password):
    login = input('Логин: ')
    password = input('Пароль: ')
    credentials = [login, password]
    # Нужна реализация функции проверки данных из БД.
    return credentials

print('Добро пожаловать пользователь.')
print('Есть аккаунт? [Да/Нет]')

# Подключение к базе данных PostgreSQL
try:
    conn = psycopg2.connect(host='localhost',
                            dbname='postgres',
                            user='postgres',
                            password='admin',
                            port='5432')
except psycopg2.Error as e:
    print(f'Ошибка при подключении к базе данных: {e}')
    exit(1)

while True:
    b = input('')
    if b == 'Нет' or b == 'нет' or b == 'НЕТ':
        credentials = entry_acc(0, 0)
        while credentials != 'exit':
            credentials = m_menu(credentials)
            if credentials != 'exit':
                break
        break
    elif b == 'Да' or b == 'да' or b == 'ДА':
        credentials = auth_acc(0, 0)
        while credentials != 'exit':
            credentials = m_menu(credentials)
            if credentials != 'exit':
                break