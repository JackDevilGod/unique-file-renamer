from pathlib import Path
from typing import Callable

from menu.get_path import user_get_path
from menu.tool_select import tool_menu
from pathing.path_container import PathContainer
from tools.no_spaces import no_spaces, no_spaces_folder
from tools.unique_file_renamer import unique_file_renamer


def main() -> None:
    user_path = user_get_path()

    contained_user_path = PathContainer(user_path)
    n_folder, n_files = contained_user_path.amount_folder_file

    print(f"selected path: {contained_user_path}")
    print(
        "This folder contains, "
        f"{n_folder} sub folders and {n_files} files total."
    )

    tool_dict: dict[str, Callable[[Path], None]] = {
        "remove spaces": no_spaces,
        "remove spaces (including folders)": no_spaces_folder,
        "rename all files to hash of content": unique_file_renamer,
        "Exit": lambda _: exit(0),
    }

    tool_menu(tool_dict, contained_user_path.base_path)


if __name__ == "__main__":
    main()
