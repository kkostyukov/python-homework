# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


import sys
# Список аргументов запуска скрипта, первым аргументом является полный путь к файлу скрипта
print('sys.argv = ', sys.argv)
# Список путей для поиска модулей
print('sys.path = ', sys.path)
# Полный путь к интерпретатору
print('sys.executable = ', sys.executable)
# словарь имен загруженных модулей
print('sys.modules = ', sys.modules)
# Информация об операционной системе
print('sys.platform = ', sys.platform)

while True:
    key = input("press 'q' to Exit")

    if key == 'q':
        sys.exit()  # Вызов данной функции мгновенно завершает работу модуля (скрипта)