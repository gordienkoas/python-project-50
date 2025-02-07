

from generate_diff import generate_diff

#file_path1 = 'file1.json'
#file_path2 = 'file2.json'


def main():
    diff = generate_diff(
        '/home/user/PycharmProjects/python-project-50/gendiff/file1.json',
        '/home/user/PycharmProjects/python-project-50/gendiff/file2.json'
    )
    print(diff)


if __name__ == '__main__':
    main()

