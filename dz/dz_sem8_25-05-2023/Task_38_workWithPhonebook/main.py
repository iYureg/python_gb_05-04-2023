def show_menu() -> int:
    print("\nВыберите действие: \n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Редактировать данные абонента\n"
          "6. Удалить абонента\n"
          "7. Закончить работу")
    choice = int(input())
    return choice

def read_file(filename: str) -> list:
    result = []
    fields = ['Фамилия', "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as data:
        for line in data:
            record = dict(zip(fields, line.strip().split(',')))
            result.append(record)
    return result

def print_result(data):
    for doc in data:
        print(*[v for k,v in doc.items()])
        

def find_by_name(name, data):
    for doc in data:
        for key, value in doc.items():
            if name.lower() == value.lower():
                return [v for k,v in doc.items()]

                
        
def find_by_number(number, data):
    for doc in data:
        for key, value in doc.items():
            if number == value:
                return [v for k,v in doc.items()]

def get_name():
    res = input("Введите имя: ")
    return res

def get_number():
    res = input("Введите номер телефона: ")
    return res

def get_surname():
    res = input("Введите фамилию пользователя: ")
    return res

   
def get_new_user():
    fields = ['Фамилия', "Имя", "Телефон", "Описание"]
    res = []
    for field in fields:
        res.append(input(f"{field}: "))
    return res

def add_user(user, filename='phonebook.csv'):
    with open(filename, 'a', encoding='utf-8') as data:
        data.write(",".join(user))
    

def write_csv(filename):
    data = read_file(filename)
    with open(filename, 'w', encoding='utf-8') as file:
        for line in data:
            file.write(",".join([v for k,v in line.items()])+"\n")
    

def get_file_name(filename= 'phon.txt'):
    filename = input("Введите имя файла: ")
    return filename

def write_txt(filename, w_data):
    data = read_file(w_data)
    with open(filename, 'w', encoding='utf-8') as file:
        for line in data:
            file.write(",".join([v for k,v in line.items()])+"\n")
    
def del_user(data, delete):
    with open('phonebook.csv','w',encoding='utf-8') as file:
        for doc in data:
            if delete != doc:
                file.write(",".join([v for k,v in doc.items()])+"\n") 

def get_user(username, data):
    for doc in data:
        for k,v in doc.items():
            if username.lower() == v.lower():
                return doc   


def upd_user(username, data):
    for doc in data:
        for k, v in doc.items():
            if username.lower() == v.lower():
                doc['Фамилия'] = input(f"Фамилия: ")        
                doc['Имя'] = input(f"Имя: ")        
                doc['Телефон'] = input(f"Телефон: ")        
                doc['Описание'] = input(f"описание: ")        

    return data            
            
def update_data(data):
    with open('phonebook.csv','w',encoding='utf-8') as file:
        for doc in data:
            file.write(",".join([v for k,v in doc.items()])+"\n")
           
def work_with_phonebook():
    choice = show_menu()
    phone_book = read_file('phonebook.csv')

    while (choice != 8):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_name()
            print(*find_by_name(name,phone_book))
        elif choice == 3:
            number = get_number()
            print(*find_by_number(number,phone_book))
        elif choice == 4:
            user_data = get_new_user()
            add_user(user_data)
            write_csv('phonebook.csv')
        elif choice == 5:
            user_surn = get_surname()
            updated_user = upd_user(user_surn, phone_book)
            update_data(updated_user)
        elif choice == 6:
            delete_user = get_user(get_surname(), phone_book)
            del_user(phone_book, delete_user)
        elif choice == 7:
            file_name = get_file_name()
            write_txt(file_name, 'phonebook.csv')
            break
        choice = show_menu()

work_with_phonebook()