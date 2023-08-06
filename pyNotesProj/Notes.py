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
    phone_book = read_file('notes.csv')

    while (choice != 6):
        if choice == 1:
            print_result(phone_book)

        choice = show_menu()


def read_file(filename: str) -> list:
    result = []
    fields = ['title', "date", "text"]
    with open(filename, 'r', encoding='utf-8') as data:
        for line in data:
            record = dict(zip(fields, line.strip().split(',')))
            result.append(record)
    return result


def print_result(data):
    for doc in data:
        print(*[v for k, v in doc.items()])
