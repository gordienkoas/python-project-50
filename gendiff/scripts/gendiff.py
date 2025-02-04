#import argparse


#def main():
    # parser = argparse.ArgumentParser(
    #     description='Compares two configuration files and shows a difference.'
    # )
    # parser.add_argument('first_file')
    # parser.add_argument('second_file')
    # parser.add_argument('-f', '--format',
    #                     default='FORMAT',
    #                     help='set format of output')
    # return parser.parse_args()

from generate_diff import generate_diff

file_path1 = 'file1.json'
file_path2 = 'file2.json'

def main():
    diff = generate_diff('/home/user/PycharmProjects/python-project-50/gendiff/file1.json', '/home/user/PycharmProjects/python-project-50/gendiff/file2.json')
    print(diff)

if __name__ == '__main__':
    main()

