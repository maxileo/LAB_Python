
# EX 1

# import os
# import sys

# def read_and_print_files(folder_path, file_extension):
#     try:
#         if not os.path.isdir(folder_path):
#             raise ValueError("Not a folder")

#         if not file_extension.startswith("."):
#             raise ValueError("Extension should start with a .")

#         files = [f for f in os.listdir(folder_path) if f.endswith(file_extension) and os.path.isfile(os.path.join(folder_path, f))]

#         if not files:
#             print(f"No files found with the extension '{file_extension}' in the folder '{folder_path}'")
#             return

#         for file_name in files:
#             file_path = os.path.join(folder_path, file_name)
#             try:
#                 with open(file_path, 'r') as file:
#                     content = file.read()
#                     print(f"Content of {file_name}:\n{content}\n\n")
#             except Exception as e:
#                 print(f"Error reading file {file_name}: {e}")

#     except Exception as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         print("Wrong arguments")
#     else:
#         directory_path = sys.argv[1]
#         file_extension = sys.argv[2]
#         read_and_print_files(directory_path, file_extension)


# EX 2

# import os
# import sys

# def rename_files(folder_path):
#     try:
#         if not os.path.isdir(folder_path):
#             raise ValueError("Invalid folder path")

#         files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

#         if not files:
#             print(f"No files found in the folder '{folder_path}'")
#             return

#         for i, file_name in enumerate(files, start=1):
#             old_path = os.path.join(folder_path, file_name)
#             new_name = f"file{i}{os.path.splitext(file_name)[1]}"
#             new_path = os.path.join(folder_path, new_name)
#             try:
#                 os.rename(old_path, new_path)
#                 print(f"Renamed {file_name} to {new_name}")
#             except Exception as e:
#                 print(f"Error renaming {file_name}: {e}")

#     except Exception as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Wrong arguments")
#     else:
#         folder_path = sys.argv[1]
#         rename_files(folder_path)


# EX 3

# import os
# import sys

# def calculate_total_size(folder_path):
#     try:
#         if not os.path.isdir(folder_path):
#             raise ValueError("Invalid folder path")

#         total_size = 0

#         for root, dirs, files in os.walk(folder_path):
#             for file_name in files:
#                 file_path = os.path.join(root, file_name)
#                 try:
#                     file_size = os.path.getsize(file_path)
#                     total_size += file_size
#                 except Exception as e:
#                     print(f"Error accessing file {file_path}: {e}")

#         print(f"Total size of all files in {folder_path}: {total_size}")

#     except Exception as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Wrong arguments")
#     else:
#         folder_path = sys.argv[1]
#         calculate_total_size(folder_path)


# EX 4

# import os
# import sys
# from collections import defaultdict

# def count_files_by_extension_recursively(folder_path):
#     try:
#         if not os.path.isdir(folder_path):
#             raise ValueError("Invalid folder path")

#         extension_counts = defaultdict(int)

#         for root, dirs, files in os.walk(folder_path):
#             for file_name in files:
#                 file_extension = os.path.splitext(file_name)[1]
#                 extension_counts[file_extension] = extension_counts[file_extension] + 1

#         if not extension_counts:
#             print(f"No files found in the folder '{folder_path}'")
#             return

#         print("File counts by extension:")
#         for extension, count in extension_counts.items():
#             print(f"{extension}: {count} files")

#     except Exception as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Wrong arguments")
#     else:
#         folder_path = sys.argv[1]
#         count_files_by_extension_recursively(folder_path)
