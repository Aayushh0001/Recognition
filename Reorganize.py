import os
import shutil
from sklearn.model_selection import train_test_split

# Define paths
source_folder = r"C:\AI\unified_dataset"  # Path to the original dataset
output_folder = r"C:\AI\organized_dataset"  # Path to the reorganized dataset

# Create subdirectories for training, validation, and testing
splits = ['training', 'validation', 'testing']
for split in splits:
    split_path = os.path.join(output_folder, split)
    os.makedirs(split_path, exist_ok=True)

# Split ratios
train_ratio = 0.8
val_ratio = 0.1
test_ratio = 0.1

# Loop through each character folder
for char_folder in os.listdir(source_folder):
    char_folder_path = os.path.join(source_folder, char_folder)
    
    if os.path.isdir(char_folder_path):  # Ensure it's a folder
        # Get all image files in the character folder
        images = [os.path.join(char_folder_path, img) for img in os.listdir(char_folder_path) if img.endswith(('png', 'jpg', 'jpeg'))]
        
        # Split into training, validation, and testing
        train_images, temp_images = train_test_split(images, test_size=(1 - train_ratio), random_state=42)
        val_images, test_images = train_test_split(temp_images, test_size=test_ratio / (val_ratio + test_ratio), random_state=42)
        
        # Define destinations
        char_train_path = os.path.join(output_folder, 'training', char_folder)
        char_val_path = os.path.join(output_folder, 'validation', char_folder)
        char_test_path = os.path.join(output_folder, 'testing', char_folder)

        # Create subfolders for each split
        os.makedirs(char_train_path, exist_ok=True)
        os.makedirs(char_val_path, exist_ok=True)
        os.makedirs(char_test_path, exist_ok=True)

        # Move files
        for img in train_images:
            shutil.copy(img, char_train_path)
        for img in val_images:
            shutil.copy(img, char_val_path)
        for img in test_images:
            shutil.copy(img, char_test_path)
        
        print(f"Processed {char_folder}: {len(train_images)} training, {len(val_images)} validation, {len(test_images)} testing images")

print("Dataset reorganization complete!")
