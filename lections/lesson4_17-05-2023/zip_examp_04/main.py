# --- функция zip ---

# функция zip применяется к набору итерируемых объектов
# возвращает итерарор с набором кортежей
# принимаемого набора данных

# input [1,2,3], ["a","b","c"], ["а","б","в"]
# output [(1,"a","а"), (2,"b","б"), (3,"c","в")]

users = ["user1", "user2", "user3", "user4", "user5"]
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

data = list(zip(users, ids))
print("zip(users, ids) -> ", data)

# по минимальному входящему набору данных
data = list(zip(users, ids, salary))
print("zip(users, ids, salary) -> ", data)
