# Телефонный справочник
import csv
import datetime

now = datetime.datetime.now()
now_string = now.strftime('%H:%M:%S %d/%m/%y')


# Функция будет записывать логфайл с ошибками.
def write_to_log(Data: str, filename='error_logfile.txt'):
    with open(filename, 'a') as output:
        output.write(now_string + ' ->   ' + Data)
        output.write('\n')


def write_to_file(contact: dict, filename='directory.csv'):
    """
    Функция которая производит запись в справочник.
    """
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        title = ['surname', 'name', 'personal_number', 'work_number', 'city', 'comment']
        writer = csv.DictWriter(csvfile, fieldnames=title, delimiter=',')
        writer.writerow(contact)

def overwrite_file(data: list, filename='directory.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        title = ['surname', 'name', 'personal_number', 'work_number', 'city', 'comment']
        writer = csv.DictWriter(csvfile, fieldnames=title, delimiter=',')
        for row in data:
            writer.writerow(dict(zip(title, row)))


def get_data_from_file(filename='directory.csv') -> list:
    """
    Функция которая считывает файл
    """
    result = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            result.append(row)
    return result


def write_contact(value: str) -> dict:
    """
    Функция которая записывает данные от пользователя в формате.
    ('surname', 'name', 'personal_number', 'work_number', 'city', 'comment')
    """
    d = ('фамилию', 'имя', 'телефон личный', 'телефон рабочий', 'город', 'примечание')
    e = ('surname', 'name', 'personal_number', 'work_number', 'city', 'comment')
    result = {}
    for i in range(len(d)):
        res = input(f'{value}{d[i]}: ')
        res = res.strip()
        result[e[i]] = res
    print(result)
    return result


def print_all_contacts(data: list) -> 'print':
    """
    Функция будет выводить все найденные контакты. На вход принимает содержимое всего файла *.csv
    """
    print('ID', 'фамилия', 'имя', 'телефон личный', 'телефон рабочий', 'город', 'примечание', sep='\t\t')
    for i, row in enumerate(data):
        print(i, *row, sep='\t\t')


def print_contacts_by_index(indexes: list):
    data = get_data_from_file()
    print('ID', 'фамилия', 'имя', 'телефон личный', 'телефон рабочий', 'город', 'примечание', sep='\t\t')
    for i, row in enumerate(data):
        if i in indexes:
            print(i, *row, sep='\t\t')


def edit_contact(value: str) -> dict:
    """
    Функция будет вносить измнения в контакт по индексу
    """
    pass


def delete_contact(del_id: str):
    """
    Функция будет удалять найденный контакт по индексу
    """
    del_id = int(del_id)
    data = get_data_from_file()
    data.pop(del_id)

    overwrite_file(data)
    print('Файл записан индексы обновлены')





def text_input(phrase: str) -> str:
    """
    Функция которая отвечает за ввод данных
    """
    result = input(phrase)
    result = result.strip()
    return result


# def parse_search_text(value: str) -> int:
#     """
#     Функция будет с выбором в главном меню. Если конечно получится перенести сюда.
#     """
#     pass

def search(value: str) -> list:  # Возвращает список индексов строк, в которых найдена строка value
    """
    Функция будет осуществлять поиск в базе по запросу. И возвращать индекс строки.
    """
    result = []
    data = get_data_from_file()
    for i, row in enumerate(data):
        for col in row:
            if value.lower() in col.lower():
                result.append(i)
    return result


def select_action(value: str) -> int:
    """
    функция будет с выбором в главном меню. Если конечно получится перенести сюда.
    """
    pass


def main():
    start = True
    general_menu = 'ГЛАВНОЕ МЕНЮ\
    \nВыберите действие\
    \n1 - добавить новый контакт.\
    \n2 - изменить запись.\
    \n3 - удалить запись.\
    \n4 - найти запись в справочнике.\
    \n5 - посмотреть весь справочник.\
    \n6 - выход из программы.\n'
    next_action = 'нажмите клавишу ENTER ...\n'
    search_text = 'Введите данные контакта, который хотите '
    error1 = 'контакт не найден'

    while start:
        value_input = 'Введите '
        gen_action = text_input(general_menu)
        if gen_action == '1':
            print('ДОБАВИТЬ КОНТАКТ')
            result = write_contact(value_input)
            write_to_file(result)
            input(f'Контакт удачно сохранен в справочник, {next_action}')
        elif gen_action == '2':
            print('ИЗМЕНИТЬ КОНТАКТ')
            result = edit_contact(f'{search_text}изменить:\n')  # обращение к поиску
            text_input(next_action)
        elif gen_action == '3':
            print('УДАЛИТЬ КОНТАКТ')
            result = text_input(f'{search_text}найти, и посмотрите его ID::\n')
            contact_indexes = search(result)  # обращение к поиску
            if len(contact_indexes) > 0:
                print_contacts_by_index(contact_indexes)
                del_id = input("Введите ID контакта, чтобы его удалить")
                delete_contact(del_id)
            else:
                print(error1)
            text_input(next_action)
        elif gen_action == '4':
            print('НАЙТИ КОНТАКТ')
            result = text_input(f'{search_text}найти:\n')  # обращение к поиску
            contact_indexes = search(result)
            if len(contact_indexes) > 0:
                print_contacts_by_index(contact_indexes)
            else:
                print(error1)
            # write_to_log(data=[result, str(error1)])
            # print(error1)
            text_input(next_action)
        elif gen_action == '5':
            print('ВЕСЬ СПРАВОЧНИК')
            data_from_file = get_data_from_file()
            print_all_contacts(data_from_file)
            text_input(next_action)
        elif gen_action == '6':
            start = False


if __name__ == '__main__':
    main()
