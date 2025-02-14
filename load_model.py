import tensorflow as tf
from tensorflow import keras
import numpy as np
import rawpy
import matplotlib.pyplot as plt
import os
import json
from matplotlib import rcParams

model = keras.models.load_model('trained_model.h5')
print("Model loaded successfully!")

with open('class_indices.json', 'r') as f:
    class_indices = json.load(f)
class_mapping = {v: k for k, v in class_indices.items()} 

img_path = r'C:\AI\organized_dataset\training\इ\001_01.jpg'

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
predicted_class_index = np.argmax(predictions, axis=1)[0]
predicted_character = class_mapping[predicted_class_index]

print(f"Predicted class: {predicted_class_index}")
print(f"Predicted character: {predicted_character}")

rcParams['font.family'] = 'Noto Sans Devanagari'

plt.imshow(img_array[0], cmap='gray')
plt.title(f"Predicted character: {predicted_character}")
plt.show()