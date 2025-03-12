from os.path import splitext

from gendiff.consts import EXTENSIONS
from gendiff.formaters import get_formatter
from gendiff.make_diff_tree import make_diff_tree
from gendiff.parser import parse


def get_file_extension(path_file: str) -> str:
    _, extension = splitext(path_file)
    return extension[1:]


def read_file_content(path_file: str) -> str:
    extension = get_file_extension(path_file)
    if extension in EXTENSIONS:
        with open(path_file, 'r') as f:
            data = f.read()
            return data, extension
    raise ValueError(f"Unrecognized extension: {extension}")


def generate_diff(path_file1: str, path_file2: str,
                  formater: str = 'stylish') -> str:
    data1, format1 = read_file_content(path_file1)
    data2, format2 = read_file_content(path_file2)
    parced_data1 = parse(data1, format1)
    parced_data2 = parse(data2, format2)
    diff = make_diff_tree(parced_data1, parced_data2)
    return get_formatter(formater)(diff)

