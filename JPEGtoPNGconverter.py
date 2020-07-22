import sys
import os
from PIL import Image

# grab the first and second argument
image_folder = sys.argv[1]
target_folder = sys.argv[2]


# check if target folder exists and if not, create it
if not os.path.exists(target_folder):
    os.makedirs(target_folder)


# loop through folder and convert it to png and save it to a target folder
for filename in os.listdir(image_folder):
    img = Image.open(f"./{image_folder}/{filename}")
    clean_name = os.path.splitext(filename)[0]
    img.save(f"./{target_folder}/{clean_name}.png", "png")
    print(f"converting {clean_name}...")

    if os.listdir(image_folder)[-1] == filename:
        print("all done!")
