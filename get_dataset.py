# Weapon Class Map: 
# {'Automatic Rifle': 0, 'Bazooka': 1, 'Handgun': 2, 'Knife': 3, 'Shotgun': 4, 'SMG': 5, 'Sniper': 6, 'Sword': 7}
import os
import random
# class GeneratingDatasetLabels:
#     def get_100_images(self):
#         # Directory containing the images
#         image_dir = "test/Test"

#         # List to store image filenames
#         all_images = []
        
#         # Collect all image files with valid extensions
#         for f in os.listdir(image_dir):
#             if f.lower().endswith(('jpg', 'png', 'jpeg')):  # Make case-insensitive
#                 all_images.append(f)

#         # Randomly sample 100 images
#         # sampled_images = random.sample(all_images, min(100, len(all_images)))

#         # Save selected images to a list or file
#         header = ["filename","label"]
#         data = []
#         for image in all_images:
#             label = image.split('_')[0]  # Get the label by splitting the filename
#             if label == "Assault":
#                 label = "Assault Rifle"
#             elif label == "Grenade":
#                 label = "Grenade Launcher"
#             data.append([image, label])  # Append the filename and label as a list
        

#         with open("final_testing.txt", "w") as file:
#             file.write(",".join(header) + "\n")  # Write the header
#             for row in data:
#                 file.write(",".join(row) + "\n")
#         return all_images


# # Example usage
# if __name__ == "__main__":
#     generator = GeneratingDatasetLabels()
#     all_images = generator.get_100_images()

# Function to rename multiple files
def main():

	folder = "test/Grenade Launcher"
	for count, filename in enumerate(os.listdir(folder)):
		dst = f"Grenade Launcher_{str(count)}.jpeg"
		src =f"{folder}/{filename}" # foldername/filename, if .py file is outside folder
		dst =f"{folder}/{dst}"
		
		# rename() function will
		# rename all the files
		os.rename(src, dst)

# Driver Code
if __name__ == '__main__':
	
	# Calling main() function
	main()

