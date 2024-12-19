# Weapon Class Map: 
# {'Automatic Rifle': 0, 'Bazooka': 1, 'Handgun': 2, 'Knife': 3, 'Shotgun': 4, 'SMG': 5, 'Sniper': 6, 'Sword': 7}
import os
import random
import shutil
class GeneratingDatasetLabels:
    def generate_label(self):
        # Directory containing the images
        image_dir = "test/Test"

        # List to store image filenames
        all_images = []
        
        # Collect all image files with valid extensions
        for f in os.listdir(image_dir):
            if f.lower().endswith(('jpg', 'png', 'jpeg')):  # Make case-insensitive
                all_images.append(f)

        # Save selected images to a list or file
        header = ["filename","label"]
        data = []
        for image in all_images:
            label = image.split('_')[0]  # Get the label by splitting the filename
            if label == "Assault":
                label = "Assault Rifle"
            elif label == "Grenade":
                label = "Grenade Launcher"
            data.append([image, label])  # Append the filename and label as a list

        with open("final_testing.txt", "w") as file:
            file.write(",".join(header) + "\n")  # Write the header
            for row in data:
                file.write(",".join(row) + "\n")
        return all_images
    
    def generate_subfolders_for_classification():
        folder = "Dataset/Phase 2 Data aug/output_geometric"
        all_images = []

        # Collect all image filenames
        for f in os.listdir(folder):
            if f.lower().endswith(('jpg', 'png', 'jpeg')):  # Make case-insensitive
                all_images.append(f)

        # Process each image
        for image in all_images:
            label = image.split('_')[0]  # Get the label by splitting the filename

            if label in image:
                src_path = os.path.join(folder, image)
                # print(src_path)

                # Create the destination folder if it doesn't exist
                dst_folder = os.path.join(folder, label)
                os.makedirs(dst_folder, exist_ok=True)

                dst_path = os.path.join(dst_folder, image)
                shutil.move(src_path, dst_path)  # Move the image
        return subfolder_generator
    
    # Function to rename multiple files
    def labeled_name_generator():
        folder = "test/Dataset/Phase 2 Data aug/output_geometric"
        for count, filename in enumerate(os.listdir(folder)):
            dst = f"Grenade Launcher_{str(count)}.jpeg"
            src =f"{folder}/{filename}" # foldername/filename, if .py file is outside folder
            dst =f"{folder}/{dst}"
            # rename all the files
            os.rename(src, dst)
        return name_generator


# Example usage
if __name__ == "__main__":
    generator = GeneratingDatasetLabels()
    all_images = generator.generate_label()
    subfolder_generator = generator.generate_subfolders_for_classification()
    name_generator = generator.labeled_name_generator()
