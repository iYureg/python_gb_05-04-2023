import time
from datetime import date


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
    notes = read_file('notes.csv')

    while (choice != 6):
        if choice == 1:
            print_result(notes)
        elif choice == 3:
            note = get_new_note()
            add_note(note, "notes.csv")

        choice = show_menu()


def read_file(filename: str) -> list:
    result = []
    fields = ['date', "title", "text"]
    with open(filename, 'r', encoding='utf-8') as data:
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
    with open(filename, 'a', encoding='utf-8') as data:
        data.write("; ".join(note) + "\n")


work_whith_notes()
