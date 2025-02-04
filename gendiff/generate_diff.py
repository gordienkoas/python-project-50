import json


def read_json_file(file_path):
    """Читает и парсит JSON файл."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def main():
    # Определите пути к файлам
    file1_path = 'file1.json'
    file2_path = 'file2.json'

    # Чтение и парсинг данных
    data1 = read_json_file(file1_path)
    data2 = read_json_file(file2_path)

    print("Данные из file1.json:")
    print(data1)

    print("\nДанные из file2.json:")
    print(data2)


if __name__ == "__main__":
    main()
