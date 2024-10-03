import os
import shutil

# Функція для рекурсивного копіювання та сортування файлів
def copy_files_recursively(source_dir, dest_dir):
    try:
        # Перевіряємо, чи існує директорія призначення, якщо ні — створюємо її
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        
        # Перебираємо всі елементи у вихідній директорії
        for item in os.listdir(source_dir):
            source_item_path = os.path.join(source_dir, item)

            # Якщо це директорія, викликаємо функцію рекурсивно
            if os.path.isdir(source_item_path):
                # Рекурсивно копіюємо файли з піддиректорії
                copy_files_recursively(source_item_path, dest_dir)
            
            # Якщо це файл, копіюємо його до відповідної піддиректорії за розширенням
            elif os.path.isfile(source_item_path):
                # Отримуємо розширення файлу
                file_extension = os.path.splitext(item)[1][1:].lower()  # Наприклад, 'txt', 'jpg'
                if file_extension == '':  # Якщо файл без розширення
                    file_extension = 'no_extension'

                # Створюємо директорію для цього розширення, якщо її не існує
                target_dir = os.path.join(dest_dir, file_extension)
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)

                # Копіюємо файл до відповідної директорії
                dest_item_path = os.path.join(target_dir, item)
                shutil.copy2(source_item_path, dest_item_path)
                print(f"Файл {item} скопійовано до {target_dir}")
    
    except PermissionError:
        print(f"Немає дозволу для доступу до {source_dir}")
    except FileNotFoundError:
        print(f"Директорія {source_dir} не знайдена")
    except Exception as e:
        print(f"Помилка: {str(e)}")

# Функція для запиту шляхів у користувача
def get_paths_from_user():
    source_directory = input("Введіть шлях до вихідної директорії: ")
    destination_directory = input("Введіть шлях до директорії призначення (за замовчуванням 'dist', яка буде створена поруч з файлом Task.py): ")

    if not destination_directory:
        destination_directory = 'dist'  # Якщо користувач не вказав директорію призначення

    return source_directory, destination_directory

if __name__ == "__main__":
    # Отримуємо шляхи від користувача
    source_directory, destination_directory = get_paths_from_user()

    # Перевіряємо, чи існує вихідна директорія
    if os.path.exists(source_directory) and os.path.isdir(source_directory):
        # Викликаємо функцію для рекурсивного копіювання файлів
        copy_files_recursively(source_directory, destination_directory)
    else:
        print(f"Вихідна директорія {source_directory} не існує або не є директорією.")
