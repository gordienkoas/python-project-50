import json


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

    keys = sorted(set(data1.keys()).union(data2.keys()))
    diff = []

    for key in keys:
        if key in data1 and key not in data2:
            diff.append(f"  - {key}: {data1[key]}")
        elif key not in data1 and key in data2:
            diff.append(f"  + {key}: {data2[key]}")
        elif data1[key] != data2[key]:
            diff.append(f"  - {key}: {data1[key]}")
            diff.append(f"  + {key}: {data2[key]}")

    return "{\n" + "\n".join(diff) + "\n}"


# Пример использования
if __name__ == "__main__":
    file_path1 = 'gendiff/file1.json'
    file_path2 = 'gendiff/file2.json'
    diff = generate_diff(file_path1, file_path2)
    print(diff)
