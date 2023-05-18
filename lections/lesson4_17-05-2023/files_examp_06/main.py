# --- работа с файлами ---

# --- режим добавления "а" ---
# colors = ['red', 'blue', 'green']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.close()

# --- режим записи "w" ---
# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')
#     data.write('line 3\n')
#     data.write('line 4\n')

# --- режим чтения "r" ---

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
