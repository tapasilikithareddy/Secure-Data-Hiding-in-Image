import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk  # Ensure both Image and ImageTk are imported

# Create the main window
root = Tk()
root.title("Steganography Project")  # Title of the window
root.geometry("400x400")  # Size of the window

# Function to upload an image
def upload_image():
    file_path = filedialog.askopenfilename()  # Open file explorer to select the image
    img = Image.open(file_path)  # Open the selected image using PIL
    img.show()  # Show the uploaded image

# Buttons for uploading image and hiding/extracting data
upload_button = Button(root, text="Upload Image", command=upload_image)
upload_button.pack()

# Run the Tkinter event loop
root.mainloop()
