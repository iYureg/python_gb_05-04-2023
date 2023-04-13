# ------ Кортежи ------

t = ()  # создание пустого кортежа
print(type(t))  # <class 'tuple'>

t = (1)
print(type(t))  # <class 'int'>

t = (1,)  # в конце запятая обязательно
print(type(t))  # <class 'tuple'>

v = [1, 5, 9]  # создание списка
print(v)
print(type(v))

v = tuple(v)  # преобразование списка в кортеж
print(v)
print(type(v))

a = b = 1
print(a, b)

a, b = 3.009323, 6.32903404
c = round(a * b, 3)
print(a, b, c)

a, b, c = v  # присваивание переменным a, b и c значений элементов кортежа
print(a, b, c)
