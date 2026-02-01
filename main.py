from pathlib import Path
from hashlib import sha256
from os import rename

from menu.get_path import user_get_path

def main():
    user_path = user_get_path()

    q: list[Path] = []

    while q:
        print(f"current queue: {len(q)}")
        current = q.pop()

        if current.is_dir():
            for child in current.iterdir():
                q.append(child)
        elif current.is_file():
            with open(current, mode="br+") as file:
                hash = sha256(file.read()).hexdigest()

                file.close()

            base_current = current.parent
            try:
                rename(current,
                       base_current.joinpath(hash + "".join(current.suffixes)))
            except FileExistsError:
                print("Found Dupe")
                current.unlink()


if __name__ == '__main__':
    main()
