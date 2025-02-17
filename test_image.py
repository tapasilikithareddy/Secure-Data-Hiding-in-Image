from PIL import Image

try:
    img = Image.open("C:/Users/91855/Downloads/test_image.jpg")  # Path to the image
    img.show()  # Display the image in the default viewer
    print("Image opened successfully!")  # To confirm the operation worked
except Exception as e:
    print(f"Error: {e}")
