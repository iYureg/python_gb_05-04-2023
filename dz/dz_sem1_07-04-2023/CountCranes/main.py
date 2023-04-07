# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

s = int(input("Введите количество журавликов: "))

if s % 3 == 0 and s % 2 == 0:
    a = s // 3 // 2
    b = a      
    c = (a + b) * 2 
    print(f"Петя -> {a}, Сережа -> {b}, Света -> {c}")
else:
    print("Что-то пошло не так")