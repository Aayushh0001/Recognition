import os

# Path to your dataset folder
dataset_folder = r"C:\AI\unified_dataset"

# Define the mapping from current folder names (e.g., vowels_1, vowels_2) to Nepali characters
folder_name_map = {
    # Vowels
    "vowels_1": "अ",  
    "vowels_2": "आ",
    "vowels_3": "इ",
    "vowels_4": "ई",
    "vowels_5": "उ",
    "vowels_6": "ऊ",
    "vowels_7": "ए",  
    "vowels_8": "ऐ",
    "vowels_9": "ओ",
    "vowels_10": "औ",
    "vowels_11": "अं",
    "vowels_12": "अः", 

    # Consonants (36 Nepali consonants)
    "consonants_1": "क",
    "consonants_2": "ख",
    "consonants_3": "ग",
    "consonants_4": "घ",
    "consonants_5": "ङ",
    "consonants_6": "च",
    "consonants_7": "छ",
    "consonants_8": "ज",
    "consonants_9": "झ",
    "consonants_10": "ञ",
    "consonants_11": "ट",
    "consonants_12": "ठ",
    "consonants_13": "ड",
    "consonants_14": "ढ",
    "consonants_15": "ण",
    "consonants_16": "त",
    "consonants_17": "थ",
    "consonants_18": "द",
    "consonants_19": "ध",
    "consonants_20": "न",
    "consonants_21": "प",
    "consonants_22": "फ",
    "consonants_23": "ब",
    "consonants_24": "भ",
    "consonants_25": "म",
    "consonants_26": "य",
    "consonants_27": "र",
    "consonants_28": "ल",
    "consonants_29": "व",
    "consonants_30": "श",
    "consonants_31": "ष",
    "consonants_32": "स",
    "consonants_33": "ह",
    "consonants_34": "क्ष",
    "consonants_35": "त्र",
    "consonants_36": "ज्ञ",

    # Numerals
    "numerals_0": "०", 
    "numerals_1": "१",  
    "numerals_2": "२",
    "numerals_3": "३",
    "numerals_4": "४",
    "numerals_5": "५",
    "numerals_6": "६",
    "numerals_7": "७",
    "numerals_8": "८",
    "numerals_9": "९",
}

# Walk through the dataset folder and rename subfolders
for root, dirs, files in os.walk(dataset_folder):
    for dir_name in dirs:
        # Check if the subfolder name exists in the map
        if dir_name in folder_name_map:
            # Get the new name from the map
            new_name = folder_name_map[dir_name]
            
            # Get the full path of the old and new folder
            old_folder_path = os.path.join(root, dir_name)
            new_folder_path = os.path.join(root, new_name)
            
            # Rename the folder
            try:
                os.rename(old_folder_path, new_folder_path)
                print(f"Renamed '{old_folder_path}' to '{new_folder_path}'")
            except Exception as e:
                print(f"Error renaming {old_folder_path}: {e}")

print("Folder renaming complete!")

