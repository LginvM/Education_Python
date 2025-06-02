def count_character_in_file(file_path, character):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()  # Читаем содержимое файла целиком
            count = content.count(character)  # Подсчитываем нужный символ
        return count
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    file_path = input("Введите путь к файлу: ")
    character = 'а'  # Символ, который мы хотим подсчитать
    count = count_character_in_file(file_path, character)
    if count is not None:
        print(f"Количество символов '{character}': {count}")