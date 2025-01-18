import os
import shutil

# Paths to dataset folders
input_folders = [
    r"C:\Users\User\Downloads\archive\nhcd\nhcd\vowels",
    r"C:\Users\User\Downloads\archive\nhcd\nhcd\numerals",
    r"C:\Users\User\Downloads\archive\nhcd\nhcd\consonants"
]
output_folder = r"C:\AI\unified_dataset"


# Iterate over each folder in the input list
for folder in input_folders:
    if not os.path.exists(folder):
        print(f"Error: Folder not found - {folder}")
        continue
    
    folder_name = os.path.basename(folder)  # Get the name of the current parent folder (e.g., "vowels,"consonants","numeraks")
    print(f"Processing folder: {folder}")
    
    # Process each subfolder (representing a character) in the current input folder
    for char_folder in os.listdir(folder):
        src = os.path.join(folder, char_folder)  # Source character folder
        
        # Create a unique name for the destination folder by combining parent folder and character folder
        unique_folder_name = f"{folder_name}_{char_folder}"
        dest = os.path.join(output_folder, unique_folder_name)  # Destination folder
        
        # Ensure it's a directory before proceeding
        if os.path.isdir(src):
            # Create destination folder if it doesn't exist
            os.makedirs(dest, exist_ok=True)
            
            # Copy files from the source folder to the destination folder
            for file in os.listdir(src):
                file_src = os.path.join(src, file)
                file_dest = os.path.join(dest, file)
                
                try:
                    shutil.copy(file_src, file_dest)  # Copy the file
                except Exception as e:
                    print(f"Error copying file {file_src}: {e}")

print("Dataset merging complete! Check the unified dataset at: C:\\AI\\unified_dataset")
