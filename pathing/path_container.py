from pathlib import Path
from queue import Queue


class PathContainer:
    def __init__(self, base_path: Path) -> None:
        self._base_path = base_path
        self._amount_folder_file: tuple[int, int] = self._count_folder_files(
            self._base_path
        )

    @property
    def amount_folder_file(self) -> tuple[int, int]:
        return self._amount_folder_file

    @property
    def base_path(self) -> Path:
        return self._base_path

    def __str__(self) -> str:
        return str(self._base_path)

    def _count_folder_files(self, base_path: Path) -> tuple[int, int]:
        n_folder = -1
        n_files = 0

        q: Queue[Path] = Queue()
        q.put(base_path)

        while not q.empty():
            current_path = q.get()

            if current_path.is_dir():
                n_folder += 1

                for child in current_path.iterdir():
                    q.put(child)

            if current_path.is_file():
                n_files += 1

        return (n_folder, n_files)


if __name__ == "__main__":
    test_object = PathContainer(Path(__file__).parent.parent)
    print(test_object)
    print(test_object.amount_folder_file)

