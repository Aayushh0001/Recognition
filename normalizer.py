import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

def normalize_image(x):
    x = x / 255.0 
    return x

datagen = ImageDataGenerator(
    preprocessing_function=normalize_image  
)

training_data = datagen.flow_from_directory(
    'organized_dataset/training',
    target_size=(28, 28),
    color_mode='grayscale',
    batch_size=32,
    class_mode='categorical'
)

images, labels = next(training_data)

print(f"First image min value: {np.min(images[0])}")
print(f"First image max value: {np.max(images[0])}")

plt.imshow(images[0], cmap='gray')
plt.title("First Image in Batch")
plt.show()
