import os
import hashlib

# Dictionary to store file hashes
file_hashes = {}

# Function to calculate file hash
def hash_file(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

# Directory path to scan for duplicate files
directory = './Fifithatlady_Nanny_Jobs'

# Walk through the directory and calculate hashes
for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        file_hash = hash_file(file_path)
        if file_hash in file_hashes:
            file_hashes[file_hash].append(file_path)
        else:
            file_hashes[file_hash] = [file_path]

# Iterate through the dictionary to find duplicate files
for file_hash, file_paths in file_hashes.items():
    if len(file_paths) > 1:
        print("Duplicate files found:")
        for file_path in file_paths:
            print(file_path)
        # Decide which file to keep and delete the rest
        # For example, you can keep the first file and delete the rest
        keep_file = file_paths[0]
        for file_to_delete in file_paths[1:]:
            os.remove(file_to_delete)
            print(f"Deleted: {file_to_delete}")

