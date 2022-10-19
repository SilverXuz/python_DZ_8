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
    with open(filename, 'a', newline='') as csvfile:
        title = ['surname', 'name', 'personal_number', 'work_number', 'city', 'comment']
        writer = csv.DictWriter(csvfile, fieldnames=title, delimiter=',')
        # for line in contact:
        #     writer.writerow(line)
        writer.writerow(contact)

def write_contact(value: str) -> dict:
    d = ('фамилию', 'имя', 'телефон личный', 'телефон рабочий', 'город', 'примечание')
    e = ('surname', 'name', 'personal_number', 'work_number', 'city', 'comment')
    result = {}
    for i in range(len(d)):
        res = input(f'{value}{d[i]}: ')
        res = res.strip()
        result[e[i]] = res
    print(result)
    return result


def print_contact(value: str) -> dict:
    """
    Функция будет выводить найденный контакт по индексу
    """
    pass

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


def show_all(filename='directory.csv'):
    """
    Функция которая выводит весь справочник
    """
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        print('фамилия', 'имя', 'телефон личный', 'телефон рабочий', 'город', 'примечание', sep='\t')
        for i, row in enumerate(reader):
            if i == 0:
                continue
            print(i, *row, sep='\t')
    # return


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

def request_search(value: str, filename='directory.csv') -> 'индекс записи':
    """
    Функция будет осуществлять поиск в базе по запросу. И возвращать индекс строки.
    """
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        # print('фамилия', 'имя', 'телефон личный', 'телефон рабочий', 'город', 'примечание', sep='\t')
        for i, row in enumerate(reader):
            # row = привести к нижнему регистру
            if value.lower() in row:
                return i
            else:
                return -1


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
            if found_contact > 0:
                print(found_contact)
            else:
                write_to_log(data=[result, str(error1)])
                print(error1)
            text_input(next_action)
        elif gen_action == '5':
            print('ВЕСЬ СПРАВОЧНИК')
            result = show_all()
            text_input(next_action)
        elif gen_action == '6':
            start = False



if __name__ == '__main__':
    main()
