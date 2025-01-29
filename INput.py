import os
import shutil

# Paths to dataset folders
input_folders = [
    r"C:\Users\User\Downloads\archive\nhcd\nhcd\vowels",
    r"C:\Users\User\Downloads\archive\nhcd\nhcd\numerals",
    r"C:\Users\User\Downloads\archive\nhcd\nhcd\consonants"
]
output_folder = r"C:\AI\unified_dataset"

for folder in input_folders:
    if not os.path.exists(folder):
        print(f"Error: Folder not found - {folder}")
        continue
    
    folder_name = os.path.basename(folder) 
    print(f"Processing folder: {folder}")
    
    for char_folder in os.listdir(folder):
        src = os.path.join(folder, char_folder)
        
        unique_folder_name = f"{folder_name}_{char_folder}"
        dest = os.path.join(output_folder, unique_folder_name)
        
        if os.path.isdir(src):
            os.makedirs(dest, exist_ok=True)
            
            for file in os.listdir(src):
                file_src = os.path.join(src, file)
                file_dest = os.path.join(dest, file)
                
                try:
                    shutil.copy(file_src, file_dest)
                except Exception as e:
                    print(f"Error copying file {file_src}: {e}")

print("Dataset merging complete! Check the unified dataset at: C:\\AI\\unified_dataset")
