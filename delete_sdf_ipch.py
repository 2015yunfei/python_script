import os
import send2trash


def move_files_to_trash(directory, extensions):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            move_files_to_trash(item_path, extensions)
        elif any(item.endswith(ext) for ext in extensions):
            send2trash.send2trash(item_path)
            print(f"Moved to trash: {item_path}")


if __name__ == "__main__":
    current_directory = os.getcwd()
    extensions_to_delete = [".ipch", ".sdf"]
    move_files_to_trash(current_directory, extensions_to_delete)
