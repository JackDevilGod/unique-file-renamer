from os import rename
from pathlib import Path
from queue import Queue


def no_spaces(base_path: Path, include_folder: bool = False) -> None:
    q: Queue[Path] = Queue()
    q.put(base_path)
    
    while not q.empty():
        current = q.get()
        
        if current.is_dir():
            for child in current.iterdir():
                q.put(child)

            if not include_folder:
                continue
            
            single_no_space(current)
        elif current.is_file():
            single_no_space(current)


def no_spaces_folder(base_path: Path) -> None:
    no_spaces(base_path, True)
            

def single_no_space(base_path: Path) -> None:
    name = base_path.stem
    no_spaces_name = "_".join(name.split(" ")) + base_path.suffix
    
    rename(base_path, base_path.parent.joinpath(no_spaces_name))
            