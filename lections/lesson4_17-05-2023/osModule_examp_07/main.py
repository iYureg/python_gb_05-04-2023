# --- Модуль OS ---

import os
# os.chdir(path) - сменить директорию
path = 'C:/Users/User/Desktop'
os.chdir(path)

# os.getcwd(path) - текущая рабочая директория

print(os.getcwd())


# os.path.abspath('file_name') - абсолютный путь к указанному файлу
print(os.path.abspath("main.py"))
