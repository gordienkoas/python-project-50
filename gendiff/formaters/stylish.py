from typing import Any

from gendiff.consts import DEFAULT_INDENT


def format_dict(value: dict, depth: int) -> str:
    lines = ['{']
    for key, nested_value in value.items():
        lines.append(f"{' ' * depth}    "
                     f"{key}: {to_str(nested_value, depth + DEFAULT_INDENT)}")
    lines.append(f'{" " * depth}}}')
    return '\n'.join(lines)


def to_str(value: Any, depth: int) -> str:
    match value:
        case dict():
            return format_dict(value, depth)
        case bool():
            return str(value).lower()
        case None:
            return 'null'
        case _:
            return str(value)


def line_forming(dictionary: dict, key: Any, depth: int, sign: str) -> str:
    return f'{" " * depth}{sign}{dictionary["key"]}: ' \
           f'{to_str(dictionary[key], depth + DEFAULT_INDENT)}'


def build_stylish_iter(diff: dict, depth=0) -> str:
    lines = ['{']
    for dictionary in diff:
        if dictionary['operation'] == 'same':
            lines.append(line_forming(
                dictionary, 'value',
                depth, sign='    '
            ))

        if dictionary['operation'] == 'add':
            lines.append(line_forming(
                dictionary, 'new',
                depth, sign='  + '
            ))

        if dictionary['operation'] == 'removed' or dictionary[
                'operation'] == 'changed':
            lines.append(line_forming(
                dictionary, 'old',
                depth, sign='  - '
            ))

        if dictionary['operation'] == 'changed':
            lines.append(
                line_forming(
                    dictionary, 'new',
                    depth, sign='  + '
                ))

        if dictionary['operation'] == 'nested':
            new_value = build_stylish_iter(dictionary['value'],
                                           depth + DEFAULT_INDENT)
            lines.append(
                f'{" " * depth}    {dictionary["key"]}: {new_value}')
    lines.append(f'{" " * depth}}}')
    return '\n'.join(lines)


def render_stylish(diff: dict) -> str:
    return build_stylish_iter(diff)