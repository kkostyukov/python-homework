import os
from pprint import pprint

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def mk_dir(name_folder, name_dir):
    try:
        os.mkdir(name_dir)
        print("Директория", name_dir, 'создана')
    except FileExistsError:
        print("Директории уже существуют")
    except FileNotFoundError:
        print("Не корректоное имя директории")
def mk_dirs():
    try:
        for i in range(9):
            os.mkdir("dir_"+str(i+1))
    except FileExistsError:
        print("Директории уже существуют")

def del_dir(name_folder, name_dir):
    try:
        os.rmdir(name_dir)
        print("Директория", name_dir, 'удалена')
    except FileNotFoundError:
        print("Директория не найдена")

def del_dirs():
    try:
        for i in range(9):
            os.rmdir("dir_"+str(i+1))
    except FileNotFoundError:
        print("Директории уже удалены")

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir():
    for obj in os.listdir():
        if os.path.isdir(obj):
            print(obj)

def list_files(name_folder):
    for obj in os.listdir():
        print(obj)
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

if __name__ == "__main__":
    pass
