import sys
import os


def create_folders(start, end):
    for i in range(start, end + 1):
        folder_name = f"编号{i}"
        try:
            os.mkdir(folder_name)
            print(f"Created folder: {folder_name}")
        except FileExistsError:
            print(f"Folder '{folder_name}' already exists.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <start_number> <end_number>")
        sys.exit(1)

    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    except ValueError:
        print("Please provide valid integer numbers for start and end.")
        sys.exit(1)

    if start >= end:
        print("Start number must be less than end number.")
        sys.exit(1)

    create_folders(start, end)
