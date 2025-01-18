import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# Define the image data generator with custom preprocessing
def normalize_image(x):
    # Normalize to [0, 1] using custom preprocessing
    x = x / 255.0  # Normalize to [0, 1]
    return x

datagen = ImageDataGenerator(
    preprocessing_function=normalize_image  # Apply custom normalization function
)

# Load the training dataset
training_data = datagen.flow_from_directory(
    'organized_dataset/training',
    target_size=(28, 28),
    color_mode='grayscale',
    batch_size=32,
    class_mode='categorical'
)

# Fetch a batch of images and labels from the training data
images, labels = next(training_data)

# Check the range of pixel values in the first image of the batch
print(f"First image min value: {np.min(images[0])}")
print(f"First image max value: {np.max(images[0])}")

# Optionally, print out the first image (in a human-readable format)
plt.imshow(images[0], cmap='gray')
plt.title("First Image in Batch")
plt.show()
