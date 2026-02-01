from pathlib import Path
from typing import Callable

from menu.help.delete_last_lines import erase_output_lines


def tool_menu(
    tool_dict: dict[str, Callable[[Path], None]],
    base_path: Path,
) -> None:
    keys = list(tool_dict.keys())

    for i, line in enumerate(keys):
        print(f"({i}): {line}")

    while True:
        user = input().strip()
        erase_output_lines(1)

        try:
            tool_id = int(user)
        except ValueError:
            continue

        if tool_id < 0 or tool_id >= len(keys):
            continue

        tool_dict[keys[tool_id]](base_path)
