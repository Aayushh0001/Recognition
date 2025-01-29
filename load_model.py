import tensorflow as tf
from tensorflow import keras
import numpy as np
import rawpy
import matplotlib.pyplot as plt
import os
from matplotlib import rcParams

# Load the trained model
model = keras.models.load_model('trained_model.h5')
print("Model loaded successfully!")

# Nepali Vowels
vowels = [
    "अ", "आ", "इ", "ई", "उ", "ऊ", "ऋ", "ए", "ऐ", "ओ", "औ", "अं", "अः"
]

# Nepali Consonants
consonants = [
    "क", "ख", "ग", "घ", "ङ", "च", "छ", "ज", "झ", "ञ",
    "ट", "ठ", "ड", "ढ", "ण", "त", "थ", "द", "ध", "न",
    "प", "फ", "ब", "भ", "म", "य", "र", "ल", "व", "श",
    "ष", "स", "ह", "क्ष", "त्र", "ज्ञ"
]

# Nepali Numerals
numerals = [
    "०", "१", "२", "३", "४", "५", "६", "७", "८", "९"
]

class_mapping = {}

for i, numeral in enumerate(numerals):
    class_mapping[i] = numeral

for i, vowel in enumerate(vowels, start=len(numerals)):
    class_mapping[i] = vowel

for i, consonant in enumerate(consonants, start=len(numerals) + len(vowels)):
    class_mapping[i] = consonant

print("Class Mapping:")
for key, value in class_mapping.items():
    print(f"{key}: {value}")


img_path = r'C:\AI\test images\IMG_5296.DNG'

file_extension = os.path.splitext(img_path)[1].lower()

if file_extension == '.dng':
    with rawpy.imread(img_path) as raw:
        rgb_image = raw.postprocess()
    img = tf.image.rgb_to_grayscale(rgb_image)
    img = tf.image.resize(img, [28, 28])
elif file_extension in ['.png', '.jpg', '.jpeg']:
    img = keras.preprocessing.image.load_img(img_path, target_size=(28, 28), color_mode='grayscale')
    img = keras.preprocessing.image.img_to_array(img)
else:
    raise ValueError("Unsupported file format")

img_array = np.expand_dims(img, axis=0)

img_array = img_array / 255.0

predictions = model.predict(img_array)
predicted_class = np.argmax(predictions, axis=1)

predicted_character = class_mapping[predicted_class[0]]

print(f"Predicted class: {predicted_class[0]}")
print(f"Predicted character: {predicted_character}")

rcParams['font.family'] = 'Noto Sans Devanagari'

plt.imshow(img_array[0], cmap='gray')
plt.title(f"Predicted character: {predicted_character}")
plt.show()
