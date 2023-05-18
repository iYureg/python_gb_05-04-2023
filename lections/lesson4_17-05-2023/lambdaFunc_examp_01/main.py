def calc1(a, b):
    return a * b


def math(op, x, y):
    print(op(x, y))


math(calc1, 5, 45)
math(lambda a, b: a*b, 5, 45)

# arr = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
# for item in arr:
#     if item % 2 == 0:
#         res.append((item, item ** 2))

# print(res)

# --- пример использования lambda функции ---


def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


data = [1, 2, 3, 5, 8, 15, 23, 38]

res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)
