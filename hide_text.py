from PIL import Image
import numpy as np

def text_to_bin(text):
    """Convert text to binary string."""
    return ''.join(format(ord(char), '08b') for char in text)

def hide_text_in_image(img_path, text, output_path):
    """Hide text in the image."""
    img = Image.open(img_path).convert('RGB')
    binary_text = text_to_bin(text) + '00000000'  # Appending null character to indicate the end
    pixels = np.array(img)
    pixel_flatten = pixels.flatten()

    for i in range(len(binary_text)):
        pixel_flatten[i] = (pixel_flatten[i] & 0b11111110) | int(binary_text[i])  # Embed the binary data into LSB

    new_pixels = pixel_flatten.reshape(pixels.shape)
    new_img = Image.fromarray(new_pixels.astype(np.uint8))
    new_img.save(output_path)
    print(f"Text hidden successfully! Image saved at {output_path}")

# Example usage
hide_text_in_image('C:\\Users\\91855\\Downloads\\test_image.jpg', 'Hello, Steganography!', 'encoded_image.png')
