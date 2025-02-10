

from generate_diff import generate_diff


def main():
    diff = generate_diff(
        '/home/user/PycharmProjects/python-project-50/gendiff/file1.json',
        '/home/user/PycharmProjects/python-project-50/gendiff/file2.json'
    )
    print(diff)


if __name__ == '__main__':
    main()

