from user_interface import *
from storage_manager import *
from termcolor import colored, cprint

while True:
        show_menu()
        contacts_list = load_contacts("contacts.json")
        command = int(input("Ваш выбор: "))
        if command == 1:
            display_message("       ---Список контактов---", "grey")
            display_contacts(contacts_list)
        elif command == 2:
            display_message("       ---Добавление нового контакта---", "grey")
            new_contact = get_new_contact_info()
            contacts_list.append(new_contact)
            save_contacts("contacts.json", contacts_list)
            display_message("Контакт успешно добавлен!", "green")
        elif command == 3:
            get_search_query()
            search = str(input()).title()
            found = False
            for contact in contacts_list:
                if contact["name"] == search or contact["phone"] == search:
                    display_message("           ---Найден контакт---", "green")
                    display_message(f"      --{contact["name"]} (тел: {contact['phone']})--", "grey")
                    found = True
                    break
            if not found:
                display_message("           ---------------------", "red")
                display_message("           --Контакт не найден--", "red")
                display_message("           ---------------------", "red")
        elif command == 0:
            display_message("До свидания!", "red")
            break
        else:
             display_message("Ошибка ввода!!!", "red")
             continue
