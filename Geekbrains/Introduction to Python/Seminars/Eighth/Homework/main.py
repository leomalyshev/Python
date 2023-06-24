# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и
# Вы должны реализовать функционал для изменения и удаления данных


# запуск
with open('myfile.txt', 'w') as fp:
    fp.write('number 1\n')
    fp.write('number 2\n')
    fp.write('number 3\n')
    fp.write('number 4\n')


# чтение
def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        return lines


# просмотр

def scan(filename):
    print("\n ФИО, номер")
    with open(filename, 'r', encoding='utf-8') as data:
        print(data.read())
    print("")

    # удаление


def delete_data(file_phone):
    print("\n ФИО, номер")
    with open(file_phone, 'r', encoding='utf-8') as data:
        tel_book = data.read()
        print(tel_book)
    print('')
    index_delete_data = int(input('Введите номер строки для удаления: ')) - 1
    tel_book_lines = tel_book.split('\n')
    del_tel_book_lines = tel_book_lines[index_delete_data]
    tel_book_lines.pop(index_delete_data)
    print(f'Удалена запись :{del_tel_book_lines} \n')
    with open(file_phone, 'w', encoding='utf-8') as data:
        data.write('\n'.join(tel_book_lines))

        # изменение


def edit_data(file_phone):
    print("\n ФИО, номер")
    with open(file_phone, 'r', encoding='utf-8') as data:
        tel_book = data.read()
    print(tel_book)
    print('')
    index_delete_data = int(input('Введите строки для редактирования: ')) - 1
    tel_book_lines = tel_book.split('\n')
    edit_tel_book_lines = edit_tel_book_lines[index_delete_data]
    elements = edit_tel_book_lines.split(' | ')
    fio = input('Введите ФИО: ')
    phone = input("Введите номер телефона: ")
    num = elements[0]
    if len(fio) == 0:
        fio = elements[1]
    if len(phone) == 0:
        phone = elements[2]
    edited_line = f"{num} | {fio} | {phone}"
    tel_book_lines[index_delete_data] = edited_line
    print(f"Запись - {edit_tel_book_lines} изменена на -{edited_line}\n")
    with open(file_phone, 'w', encoding='utf-8') as f:
        f.write('\n'.join(tel_book_lines))


# поиск
def search(data):
    count = 1
    name = input('имя > ')
    for line in data:
        if name in line:
            count = 0
            print(line)
    if count: print('no name given')


data = read_file('myfile.txt')
dict_command = {'1': scan, '2': search}  # словарь команд, в значениях функции их исполняющие

print('''Команды для работы co справочником:
    Просмотр всех записей справочника:  - 1
    Поиск по справочнику -2
    Добавление новой записи - 3
    Удаление записи из справочника по Имени и Фамилии - 4
    Изменение любого поля в определенной записи справочника - 5 
    Вывод возраста человека (записи) по Имени и Фамилии - 6 ''')

while True:
    command = input('Команда: > ')
    if command in dict_command:
        dict_command[command](data)
    else:
        print(' command error!')