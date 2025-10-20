import json
from termcolor import cprint

def load_contacts(file_path: str) -> list[dict]:
    try:
        with open(file_path,"r", encoding="utf-8") as f:
            data = []
            data = json.load(f)
            return data
    except FileNotFoundError:
        cprint("Файл не найден!", "red")

def save_contacts(file_path: str, contacts: list[dict]):
    with open(file_path,"w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)