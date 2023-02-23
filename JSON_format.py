import json


def load():  
    fname = 'PhoneBook_bd.json'  
    with open(fname, 'r', encoding='utf-8') as fh:  
        phone_data = json.load(fh)  
    print('Справочник успещно загружен')
    print()
    return phone_data


def save(phone_book):  
    with open('PhoneBook_bd.json', 'w', encoding='utf-8') as fh:  
        fh.write(json.dumps(phone_book,
                            ensure_ascii=False))  
    print('Справочник обновлен')
    print()
