from hashlib import sha256
from os import rename
from pathlib import Path
from queue import Queue


def unique_file_renamer(base_path: Path) -> None:
    q: Queue[Path] = Queue()
    q.put(base_path)

    while not q.empty():
        current = q.get()

        if current.is_dir():
            for child in current.iterdir():
                q.put(child)

        elif current.is_file():
            with open(current, mode="rb") as file:
                content_hash = sha256(file.read()).hexdigest()

            base_current = current.parent
            try:
                rename(
                    current,
                    base_current.joinpath(
                        content_hash + "".join(current.suffixes)
                    ),
                )
            except FileExistsError:
                current.unlink()
