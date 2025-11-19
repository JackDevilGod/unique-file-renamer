from pathlib import Path
from os import rename
import hashlib


def main():
    path = r""
    actual_path = Path(path)

    queue = [actual_path]
    while queue:
        current = queue.pop(0)

        if current.is_dir():
            for child in current.iterdir():
                queue.append(child)
        elif current.is_file():
            h = hashlib.sha256(str(current.resolve()).encode("utf-8")).hexdigest()

            suffix = current.suffix
            parent = current.parent
            target = parent / f"{h}{suffix}"
            counter = 1
            while target.exists():
                target = parent / f"{h}_{counter}{suffix}"
                counter += 1

            rename(str(current), str(target))


if __name__ == '__main__':
    main()
