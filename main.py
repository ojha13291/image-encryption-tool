import tkinter as tk
from tkinter import filedialog
from PIL import Image
import numpy as np

# Function to swap pixels of two images
def swap_pixels(image):
    pixels = np.array(image)
    swapped_pixels = np.flip(pixels, axis=(0, 1))
    return Image.fromarray(swapped_pixels)

# Function to apply a basic mathematical operation to each pixel
def apply_math_operation(image, operation_value):
    pixels = np.array(image)
    modified_pixels = np.clip(pixels + operation_value, 0, 255)
    return Image.fromarray(modified_pixels.astype(np.uint8))

# Function to display images
def display_image(image, title):
    image.show(title=title)

# Function to open file dialog and choose image
def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image files", ".jpg;.jpeg;.png;.bmp")])
    return file_path

# Open the file dialog to select an image
input_image_path = open_file_dialog()

if input_image_path:
    # Load the selected image
    image = Image.open(input_image_path)

    # Display original image
    display_image(image, "Original Image")

    # Perform pixel swap operation
    swapped_image = swap_pixels(image)
    display_image(swapped_image, "Swapped Image")

    # Apply a basic mathematical operation (e.g., adding 50 to each pixel's value)
    modified_image = apply_math_operation(image, 50)
    display_image(modified_image, "Modified Image")

    # Save the encrypted images
    swapped_image.save('swapped_image.jpg')
    modified_image.save('modified_image.jpg')

else:
    print("No image selected")