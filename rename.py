import os

def rename_files_by_extension(folder_path):
    if not os.path.isdir(folder_path):
        print("Invalid folder path")
        return

    files = os.listdir(folder_path)

    # Dictionary to keep counters per extension
    counters = {}

    for file in files:
        full_path = os.path.join(folder_path, file)

        # Skip directories
        if not os.path.isfile(full_path):
            continue

        name, ext = os.path.splitext(file)

        # Normalize extension (optional: lower case)
        ext = ext.lower()

        if ext not in counters:
            counters[ext] = 1

        new_name = f"{counters[ext]}{ext}"
        new_full_path = os.path.join(folder_path, new_name)

        # Handle name conflicts
        while os.path.exists(new_full_path):
            counters[ext] += 1
            new_name = f"{counters[ext]}{ext}"
            new_full_path = os.path.join(folder_path, new_name)

        os.rename(full_path, new_full_path)
        print(f"Renamed: {file} -> {new_name}")

        counters[ext] += 1


if __name__ == "__main__":
    folder = input("Enter folder path: ").strip()
    rename_files_by_extension(folder)