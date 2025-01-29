import os

model_path = r"C:\AI\trained_model.h5"

if os.path.exists(model_path):
    os.remove(model_path)
    print(f"Model {model_path} has been deleted.")
else:
    print(f"Model {model_path} does not exist.")
