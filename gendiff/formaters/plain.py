from typing import Any, Union


def to_str(value: Any) -> Union[str, int]:
    match value:
        case dict():
            return "[complex value]"
        case bool():  # Булевое значение будет правильно обработано
            return str(value).lower()
        case None:
            return "null"
        case int():
            return value
        case _:
            return f"'{value}'"


def build_plain_iter(diff: dict, path="") -> str:
    lines = list()
    for dictionary in diff:
        property = f"{path}{dictionary['key']}"

        if dictionary['operation'] == 'add':
            lines.append(f"Property '{property}' "
                         f"was added with value: "
                         f"{to_str(dictionary['new'])}")

        if dictionary['operation'] == 'removed':
            lines.append(f"Property '{property}' was removed")

        if dictionary['operation'] == 'nested':
            new_value = build_plain_iter(dictionary['value'], f"{property}.")
            lines.append(f"{new_value}")

        if dictionary['operation'] == 'changed':
            lines.append(f"Property '{property}' was updated. "
                         f"From {to_str(dictionary['old'])} to "
                         f"{to_str(dictionary['new'])}")
    return '\n'.join(lines)


def render_plain(diff: dict) -> str:
    return build_plain_iter(diff)