# Weapon Class Map: 
# {'Automatic Rifle': 0, 'Bazooka': 1, 'Grenade Launcher': 2, 'Handgun': 3, 'Knife': 4, 'Shotgun': 5, 'SMG': 6, 'Sniper': 7, 'Sword': 8}

import os
import random

class GeneratingDatasetLabels:
    def get_100_random_images(self):
        # Directory containing the images
        image_dir = "Dataset/images"

        # List to store image filenames
        all_images = []
        
        # Collect all image files with valid extensions
        for f in os.listdir(image_dir):
            if f.lower().endswith(('jpg', 'png', 'jpeg')):  # Make case-insensitive
                all_images.append(f)

        # Randomly sample 100 images
        sampled_images = random.sample(all_images, min(100, len(all_images)))

        # Print the sampled images (for verification)
        print(f"Randomly Selected {len(sampled_images)} Images:")
        print(sampled_images)
        # Save selected images to a list or file
        with open("random_images.txt", "w") as file:
            file.writelines("\n".join(sampled_images))
        # Return the sampled images
        return sampled_images

# Example usage
if __name__ == "__main__":
    generator = GeneratingDatasetLabels()
    sampled_images = generator.get_100_random_images()


