from storage_manager import *
from termcolor import cprint

def show_menu() -> str:
    display_message("           ---Меню---")
    display_message("1. Показать все контакты", "grey")
    display_message("2. Добавить контакт", "grey")
    display_message("3. Найти контакт", "grey")
    display_message("0. Выход", "grey")

def get_new_contact_info() -> dict:
    while True:
        new_name = input("Введите имя нового контакта(Например, Иван Иванов): ").title()
        new_phone = input("Введите номер нового контакта(Например, 621-52-24): ")
        if new_name == "" or new_phone == "":
            display_message("Поле не может быть пустым", "red")
            continue
        elif len(new_name) < 3 or len(new_phone) < 9:
            display_message("Введите корректное значение", "red")
        elif new_name.isnumeric():
            display_message("Поле с именем не может быть числом", "red")
        elif not new_phone.isnumeric():
            display_message("Поле с номером не может быть строкой", "red")
            continue
        else:break
        
    new_contact = {
        "name" : new_name,
        "phone" : new_phone
    }
    return new_contact

def get_search_query() -> str:
    print("Введите имя или номер: ")

def display_contacts(contacts: list[dict]):
    num = 1
    for contact in contacts:
        print(f"{num}. {contact["name"]} (тел: {contact["phone"]})")
        num+=1

def display_message(message: str, color : str = "white"):
    cprint(message, color)