from PhoneBook_lib import *
from JSON_format import *


welcome()  # Ввод приветствия программы


try:    # Загрузка данных из файла
    phone_book = load()
except:
    phone_book = {}
    print("Справочник пуст. Добавьте запись.")
    print()


while True:
    menu()  # Вывод пунктов меню
    choice = int(input("Ваш выбор: "))

    if choice == 1:  # Вывести телефонный справочник на экран
        show(phone_book)

    elif choice == 2:  # Добавить запись
        new_record(phone_book)

    elif choice == 3:  # Поиск контакта
        search_record(phone_book)

    elif choice == 4:  # Редактирование записи
        edit_record(phone_book)

    elif choice == 5:  # Удалить запись
        delete_record(phone_book)

    elif choice == 6:  # Сохранить в файл
        save(phone_book)

    elif choice == 0:  # Закрыть программу
        print("Всего хорошего")
        save(phone_book)
        break
    else:
        print("Не существует")
