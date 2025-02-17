from PIL import Image
import numpy as np

def bin_to_text(binary):
    """Convert binary string to text."""
    text = ''
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if byte == '00000000':  # Stop when null byte is encountered
            break
        text += chr(int(byte, 2))
    return text

def extract_text_from_image(img_path):
    """Extract hidden text from the image."""
    img = Image.open(img_path).convert('RGB')
    pixels = np.array(img)
    pixel_flatten = pixels.flatten()
    
    binary_text = ''.join(str(pixel_flatten[i] & 1) for i in range(len(pixel_flatten)))  # Extract binary data from LSB
    extracted_text = bin_to_text(binary_text)  # Convert binary data back to text
    print(f"Extracted Text: {extracted_text}")
    return extracted_text

# Example usage
extract_text_from_image('encoded_image.png')
