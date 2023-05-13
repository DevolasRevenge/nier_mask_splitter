from PIL import Image
import os

# gets path of current directory
current_dir = os.getcwd()

# path for converted mask maps
mask_folder = current_dir + "\\converted_mask_maps"

# suffix for replicant orm maps
file_suffix = "orm.png"

image_list = []

#checks for a folder and creates it if it doesn't exist
def folder_check(folder):
    if not os.path.exists(folder):
        try: 
            os.mkdir(folder) 
        except OSError as error: 
            print(error)  

def separate_and_combine(image_path, image_name):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to RGB mode
    image = image.convert("RGB")

    # Split the image into individual color channels
    red, green, blue = image.split()

    # Invert the green channel
    inverted_green = green.point(lambda x: 255 - x)

    print("RGB channels split for " + str(image_name))

    # Merge in a different order
    combined_image = Image.merge("RGB", (blue, inverted_green, red))

    # Save the combined image
    combined_image.save(os.path.join(mask_folder, image_name))

    print("RGB channels combined for " + str(image_name))  

def image_list_maker():
    for f in os.listdir(current_dir):
        endswith = f.endswith(file_suffix)
        if endswith == True:
            image_list.append(f)

def image_iteration():
    for image in image_list:
        image_path = os.path.join(current_dir, image)
        image_name = image
        separate_and_combine(image_path, image_name)

    print("Complete...")

    
# Call the function with the path to your image
folder_check(mask_folder)
image_list_maker()
image_iteration()

