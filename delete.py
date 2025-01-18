import os

# Path to your saved model file
model_path = r"C:\AI\trained_model.h5"

# Delete the model file
if os.path.exists(model_path):
    os.remove(model_path)
    print(f"Model {model_path} has been deleted.")
else:
    print(f"Model {model_path} does not exist.")
