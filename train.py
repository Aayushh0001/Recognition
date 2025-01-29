import os
import tensorflow as tf
from tensorflow import keras
from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import json

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

model = keras.Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(training_data.num_classes, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(
    training_data,
    epochs=20, 
    validation_data=validation_data
)

test_loss, test_acc = model.evaluate(testing_data)
print(f"Test accuracy: {test_acc}")

model.save('trained_model.h5')
print("Model saved as 'trained_model.h5'")

class_indices = training_data.class_indices
with open('class_indices.json', 'w') as f:
    json.dump(class_indices, f)
print("Class indices saved to 'class_indices.json'")