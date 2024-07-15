import os

def count_files_by_extension(directory):
    file_count = {}
    other_count = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext:
                ext = ext[1:].lower()  
                file_count[ext] = file_count.get(ext, 0) + 1
            else:
                other_count += 1

    return file_count, other_count

def display_summary(directory):
    file_count, other_count = count_files_by_extension(directory)

    summary = "Summary:\n"
    for ext, count in file_count.items():
        summary += f"{ext} = {count}, "
    summary += f"other = {other_count}"

    print(summary)

def main():
    directory = input("Enter directory path: ")
    display_summary(directory)

if __name__ == "__main__":
    main()
