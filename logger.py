import os
from data_create import name_data, surname_data, telephone_data, adress_data

file_name = "data.txt"
def print_data():
    if os.path.exists(file_name):
       print('Ввывод данных из файла: ')
       with open(file_name, 'r', encoding="utf-8") as file:
           list_data = file.readlines()
           for element in list_data:
               print(element)
    else:
        print("Файла не существует!!!")

def input_data():
    print('Введите данные для записи в файл: ')
    name = name_data()
    surname = surname_data()
    telephone = telephone_data()
    adress = adress_data()
    with open(file_name, "a", encoding="utf-8" ) as file:
        file.write(f"{name}; {surname}; {telephone}; {adress}\n")

def filter_data(filter_string):
    with open (file_name, 'r', encoding="utf-8") as file:
        list_data = file.readlines()
        if ";" in filter_string:
            list_filter = filter_string.split(";")
        else:
            list_filter = [filter_string]
        is_found = False

        for element in list_data:
            temp_record = element.split(";")
            count = 0
            for record in temp_record:
                for element_filter in list_filter:

                    if element_filter.lower() in record.lower() and len(element_filter.lower()) == len(record.lower()):
                       count += 1

            if count == len(list_filter):
                print(element)
                is_found = True
    if not is_found:
        print("Таких записей не найденно! ")

def delete_contact(el):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = list.readlines()
        with open (file_name, 'r', encoding='utf-8') as file:
            for line in lines:
                if el not in line:
                    list.write(line)
                    print("Успешно удалено: ")
    delete_contact()

def replace_contact(el):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = list.readlines()
        with open (file_name, 'w', encoding='utf-8') as file:
            for line in lines:
                if el not in line:
                    line = line.split()
                    for part in line:
                        new_note = part.replace(part, input(f'Введите новую информацию вместо {part} => '))
                        list.writelines(new_note + '')
                        print('Готово!')
                else:
                    list.write(str(line))
    replace_contact()

