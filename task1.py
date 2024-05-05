import os
import shutil
import sys

def copy_files(source_dir, dest_dir):
    # перевірка, чи існує задана директорія з файлами
    if not os.path.exists(source_dir):
        print(f"Директорії {source_dir} не існує.")
        return

    # перевірка, чи існує директорія призначення
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # читаємо вміст директорії
    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)

        # запускаємо рекурсію
        if os.path.isdir(item_path):
            copy_files(item_path, dest_dir)
        else:
            # якщо це файл, копіюємо його відповідної папки
            filename, file_extension = os.path.splitext(item)
            file_extension = file_extension[1:]  # видаляємо крапку перед розширенням

            # створюємо піддиректорію, яка має назву як розширення файлу, якщо її ще не існує
            file_dest_dir = os.path.join(dest_dir, file_extension)
            if not os.path.exists(file_dest_dir):
                os.makedirs(file_dest_dir)

            # копіюємо файл у відповідну піддиректорію
            try:
                shutil.copy(item_path, file_dest_dir)
                print(f"Скопійовано {item} до {file_dest_dir}")
            except Exception as err:
                print(f"Помилка копіювання {item}: {err}")

def main():
    # парсимо аргументи командного рядка
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    if not dest_dir:
        dest_dir = "dist"  #якщо папка не передана в командній строці

    copy_files(source_dir, dest_dir)

if __name__ == "__main__":
    main()
