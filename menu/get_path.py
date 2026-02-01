from pathlib import Path

from help.delete_last_lines import erase_output_lines

def user_get_path() -> Path:
    print("Input directory you want this tool to work on")

    while True:
        path: str = input()
        
        user_path = Path(path)

        if not user_path.exists():
            erase_output_lines(1)
            continue
        
        erase_output_lines(2)
        return user_path

if __name__ == "__main__":
    user_get_path()
    print("adawdad")
    while True:
        pass
