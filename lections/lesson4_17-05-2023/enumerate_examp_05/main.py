# --- Функция enumerate ---

# Функция enumerate() применяется к итерируемому объекту
# и возвращает новый итератор с
# кортежами из индекса и элементов входных данных.


print("list(enumerate(['user1', 'user2', 'user3'])) - > ",
      list(enumerate(['user1', 'user2', 'user3'])))

citys = ["Казань", "Смоленск", "Рыбки", "Токио"]
result = list(enumerate(citys))
print("enumerate(citys) -> ", result)
