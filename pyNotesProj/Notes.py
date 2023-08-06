import os
import time
from datetime import date


def clear(): return os.system('cls')


def show_menu() -> int:
    print("\n>> Menu <<: \n"
          "1. Показать все заметки\n"
          "2. Показать конкретную заметку\n"
          "3. Добавить новую заметку\n"
          "4. Редактировать заметку\n"
          "5. Удалить заметку\n"
          "6. Закончить работу\n")
    choice = int(input())
    return choice


def work_whith_notes():
    choice = show_menu()
    notes = read_file("notes.csv", "a+")

    while (choice != 0):
        choice = show_menu()
        print("_____________")
        if choice == 1:
            notes = read_file("notes.txt")
            clear()
            print_result(notes)
        elif choice == 2:
            note_title = input("Введите заголовок заметки: ")
            notes = read_file("notes.csv")
            note = get_note(note_title, notes)
            if (note):
                clear()
                print_note(note)
            else:
                clear()
                print("Заметка не найдена")

        elif choice == 3:
            note = get_new_note()
            add_note(note, "notes.csv")
            clear()

        elif choice == 6:
            clear()
            print("Завершение работы")
            break


def read_file(filename: str, param: str = "r") -> list:
    result = []
    fields = ['date', "title", "text"]
    with open(filename, param, encoding='utf-8') as data:
        for line in data:
            record = dict(zip(fields, line.strip().split('; ')))
            result.append(record)
    return result


def print_result(data):
    for doc in data:
        print(*[v for k, v in doc.items()])


def get_new_note():
    res = []
    res.append(str(date.fromtimestamp(time.time())))
    res.append(input("Заголовок: "))
    res.append(input("Текст заметки: "))

    return res


def add_note(note, filename):
    with open(filename, 'a+', encoding='utf-8') as data:
        data.write("; ".join(note) + "\n")


def get_note(note_title, notes):
    for note in notes:
        for k, v in note.items():
            if note_title.lower() == v.lower():
                return note


def print_note(note):
    for k, v in note.items():
        print(k + ": " + v)


work_whith_notes()
