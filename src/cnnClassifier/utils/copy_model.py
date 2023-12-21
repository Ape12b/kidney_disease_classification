import shutil
import os

def copy_file(src_folder, dest_folder, filename):
    # Construct the full path for the source file
    src_path = os.path.join(src_folder, filename)

    # Construct the full path for the destination file
    dest_path = os.path.join(dest_folder, filename)

    # Create folder if it doesn't exist
    if not os.path.exists(dest_folder):
        # If it doesn't exist, create the folder and its parents if necessary
        os.makedirs(dest_folder)
        
    # Use shutil.copy2 to copy the file along with metadata
    shutil.copy2(src_path, dest_path)

# Example usage:
source_folder = "artifacts/model_training"
destination_folder = "model"
file_to_copy = "model.h5"

copy_file(source_folder, destination_folder, file_to_copy)