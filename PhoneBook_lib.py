from JSON_format import *

version = "v.0.1"
straights = "=" * 23
straights2 = "-" * 23


def welcome():
    print()
    print("=== PhoneBook", version, "===")
    print(straights)


def menu():
    print("Режимы работы: \n"
          "1. Вывести телефонный справочник на экран \n"
          "2. Добавить запись \n"
          "3. Поиск контакта \n"
          "4. Редактировать запись \n"
          "5. Удалить запись \n"
          "6. Сохранить в файл \n"
          "0. Закрыть программу")
    print(straights)


def show(book):
    print("=== Телефонный справочник ===")
    print()
    for k, v in book.items():
        print(k, " - ", end=" | ")
        for i, j in v.items():
            if j != "":
                print(i, j, end=" | ")
        print()
    print(straights)


def new_record(book):
    user_name = input("Введите имя контакта ")
    dict = {}
    dict['phone'] = list(map(int, input(
        'Введите номер телефона (если номеров несколько, вводите через пробел) ').split()))
    dict['birthday'] = input('Введите дату рождения ')
    dict['email'] = input('Введите e-mail ')
    book[user_name] = dict
    save(book)


def search_record(book):
    search_word = input("Введите имя контакта: ")
    print("=== Результат поиска ===")
    flask = True
    for key in book:
        for word in range(len(key.split())):
            if search_word == key.split()[word]:
                print(key, " - ", end="")
                for k, v in book[key].items():
                    if v != "":
                        print(k, v, end=" | ")
                flask = False
    if flask:
        print("Введенного имени не существует")
    print()
    print(straights)


def edit_record(book):
    search_word = input("Введите имя контакта: ")
    flask = True
    dict = {}
    for key in book:
        for word in range(len(key.split())):
            if search_word == key.split()[word]:
                print("Что необходимо отредактировать: \n"
                      "1. Номер телефона \n"
                      "2. Дата рождения \n"
                      "3. e-mail \n"
                      "0. Закрыть редактирование \n")
                choice = int(input("Ваш выбор: "))
                if choice == 1:
                    dict['phone'] = list(map(int, input(
                        'Введите номер телефона (если номеров несколько, вводите через пробел) ').split()))
                    book[key].update(phone=dict['phone'])
                elif choice == 2:
                    dict['birthday'] = input('Введите дату рождения ')
                    book[key].update(birthday=dict['birthday'])
                elif choice == 3:
                    dict['email'] = input('Введите e-mail ')
                    book[key].update(email=dict['email'])
                elif choice == 0:
                    break
                flask = False
                save(book)
    if flask:
        print("Введенного имени не существует")
    print()
    print(straights)


def delete_record(phone_book):
    user_name = input("Введите имя контакта для удаления: ")
    if user_name in phone_book:
        phone_book.pop(user_name)
        print(f"### Запись {user_name} удалена ###")
    else:
        print("Введенного имени не существует")
