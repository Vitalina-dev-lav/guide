from logger import input_data, print_data,filter_data,delete_contact,replace_contact

def interface():
    print("""Выберите режим работы: 
              1 - Запись данных
              2 - Ввывод данных
              3 - Поиск данных по параметрам
              4 - Удаление данных
              5 - Изменение информации
              """)
    command_number = int(input("Введите номер команды: "))
    while command_number < 1 or command_number > 5:
        print("Введите корректный номер команды: ")
        command_number = int(input("Введите номер команды: "))

    if command_number == 1:
        input_data()
    elif command_number == 2:
        print_data()
    elif command_number == 3:
        print("Введите параметры поиска через ';' :")
        filter_string = input()
        filter_data(filter_string)
    elif command_number == 4:
        print("Введите какие данные удалить: ")
        delete_contact()
    elif command_number == 5:
        replace_contact()