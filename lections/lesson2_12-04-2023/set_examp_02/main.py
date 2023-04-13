# Операции со множествами в Python:
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}

c = a.copy()    # копирование   # c = {1, 2, 3, 5, 8}
u = a.union(b)  # объединение     # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b)  # пересечения          # i = {8, 2, 5}
dl = a.difference(b)   # разность   a - b     # dl = {1, 3}
dr = b.difference(a)   # разность   b - a     # dr = {13, 21}

# выражение методов
#       2           3             1
q = a.union(b).difference(a.intersection(b))  # {1, 21, 3, 13}
