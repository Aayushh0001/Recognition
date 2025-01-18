import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np

def normalize_image(x):
    # Normalize to [0, 1] using custom preprocessing
    x = x / 255.0  # Normalize to [0, 1]
    return x

# Define the image data generator with custom preprocessing
datagen = ImageDataGenerator(
    preprocessing_function=normalize_image  # Apply custom normalization function
)

# Load the training, validation, and testing datasets as usual
training_data = datagen.flow_from_directory(
    'organized_dataset/training',
    target_size=(28, 28),
    color_mode='grayscale',
    batch_size=32,
    class_mode='categorical'
)

validation_data = datagen.flow_from_directory(
    'organized_dataset/validation',
    target_size=(28, 28),
    color_mode='grayscale',
    batch_size=32,
    class_mode='categorical'
)

testing_data = datagen.flow_from_directory(
    'organized_dataset/testing',
    target_size=(28, 28),
    color_mode='grayscale',
    batch_size=32,
    class_mode='categorical'
)

print("Datasets loaded successfully!")
