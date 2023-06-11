from db import database_init, get_connection


def get_queryset(number, cursor):
    if number == 1:
        sql_text = "SELECT priority, name, work, path FROM workers"
    if number == 2:
        sql_text = "SELECT  priority, name FROM workers"
    if number == 3:
        sql_text = "SELECT  priority, name, path FROM workers"
    list_priority = list(range(0, 4))
    error_message = f'Выберите число от {list_priority[0]} до {list_priority[-1]}'
    print('Выберите приоритет по должностям от 1 до 3, если нужно вывести все приоритеты, то введите 0')
    number_priority = choice_number(list_priority, error_message)
    if number_priority == 0:
        pass
    else:
        sql_text += f' WHERE priority={number_priority}'

    cursor.execute(sql_text)
    queryset = cursor.fetchall()
    query_result = [print(dict(line)) for line in
                    [zip([column[0] for column in cursor.description], row) for row in queryset]]


def print_message():
    hello_text = 'Здравствуйте, выберите нужные данные' \
                 '1 Отобразить все данные (порядок данных: 5, 2, 3, 4) \n' \
                 '2 Отобразить должность, имя (порядок данных: 5, 2) \n' \
                 '3 Отобразить должность, имя, подразделение (порядок данных: 5, 2, 4) \n'
    print(hello_text)


def choice_number(range_list, error_message):
    try:
        number = int(input())
    except:
        print('Введите число')
        number = choice_number(range_list, error_message)
    if number not in range_list:
        print(error_message)
        number = choice_number(range_list, error_message)
    return number


if __name__ == '__main__':
    database_init()
    cursor = get_connection()
    print_message()
    range_list = list(range(1, 4))
    error_message = f'Выберите число от {range_list[0]} до {range_list[-1]}'
    number = choice_number(range_list, error_message)
    queryset = get_queryset(number, cursor)
