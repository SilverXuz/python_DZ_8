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


def write_to_directory(contact: dict, filename='directory.csv'):
    """
    Функция которая производит запись в справочник.
    """
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        title = ['surname', 'name', 'personal_number', 'work_number', 'city', 'comment']
        writer = csv.DictWriter(csvfile, fieldnames=title)
        writer.writerow(contact)


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


def print_contacts(data) -> 'print':
    """
    Функция будет выводить все найденные контакты в файле. На вход принимает содержимое всего файла *.csv
    """
    for i, row in enumerate(data):
        if i == 0:
            print('ID', 'фамилия', 'имя', 'телефон личный', 'телефон рабочий', 'город', 'примечание', sep='\t')
        print(i, *row, sep='\t')


def print_find_contacts(data, index) -> 'print':
    """
    Функция будет выводить все строки по индексу с найденными совпадениями поиска
    """
    for i, row in enumerate(data):
        if i == 0:
            print('ID', 'фамилия', 'имя', 'телефон личный', 'телефон рабочий', 'город', 'примечание', sep='\t')
        elif i == index:
            print(i, *row, sep='\t')


def edit_contact(value: str) -> dict:
    """
    Функция будет вносить измнения в контакт по индексу
    """
    pass

def delete_contact(value: str) -> dict:
    """
    Функция будет удалять найденный контакт по индексу
    """
    pass


def get_data_from_file(filename='directory.csv'):
    """
    Функция которая считывает файл
    """
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        x = [row for row in reader]
    return x


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

def request_search(value: str, filename='directory.csv') -> int:
    """
    Функция будет осуществлять поиск в базе по запросу. И возвращать индекс строки.
    """
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            for col in row:
                if value.lower() in col.lower():
                    return i


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
            write_to_directory(result)
            input(f'Контакт удачно сохранен в справочник, {next_action}')
        elif gen_action == '2':
            print('ИЗМЕНИТЬ КОНТАКТ')
            result = edit_contact(f'{search_text}изменить:\n') # обращение к поиску
            text_input(next_action)
        elif gen_action == '3':
            print('УДАЛИТЬ КОНТАКТ')
            result = edit_contact(f'{search_text}удалить:\n') # обращение к поиску
            text_input(next_action)
        elif gen_action == '4':
            print('НАЙТИ КОНТАКТ')
            result = text_input(f'{search_text}найти:\n')  # обращение к поиску
            found_contact = request_search(result)

            print_find_contacts(str(get_data_from_file), found_contact)
            text_input(next_action)
        elif gen_action == '5':
            print('ВЕСЬ СПРАВОЧНИК')
            data_from_file = get_data_from_file()
            print_contacts(data_from_file)
            text_input(next_action)
        elif gen_action == '6':
            start = False



if __name__ == '__main__':
    main()
