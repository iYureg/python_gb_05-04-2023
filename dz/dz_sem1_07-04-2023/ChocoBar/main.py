# Задача 8: 
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
#  если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no
print('--- Введите размер шоколадки ---')
x = int(input('Введите x: '))
y = int(input('Введите y: '))

s = x * y
k = s - int(input('Сколько отломить? ')) 

if (k % x == 0 or k % y == 0) and k < s:
    print("Можно отломить")
else:
    print("Извините, оломить нельзя")
