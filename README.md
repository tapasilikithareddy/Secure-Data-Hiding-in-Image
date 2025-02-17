# Secure Data Hiding in Image using Steganography

## Description
This project focuses on **secure data hiding** in an image using **steganography**. It allows you to hide sensitive information in an image without any visible alteration. The hidden data can be extracted later. This technique ensures that the data remains invisible to unauthorized parties and protects privacy.

## Problem Statement
The project aims to develop a technique to hide data securely in images, preventing unauthorized access to the hidden information. In today’s digital world, protecting sensitive data and ensuring secure communication is crucial.

## Technology Used
- **Python**: The primary programming language for this project due to its simplicity and extensive support for image processing.
- **OpenCV**: Used for image manipulation and processing.
- **NumPy**: Used for efficient handling of pixel data in the image.
- **Pillow (PIL)**: For opening, editing, and saving images.
- **Tkinter**: For developing a user-friendly graphical interface.
- **GitHub**: For version control and collaboration.

## Features
- **Data Hiding**: Secure data can be hidden in an image file, maintaining the image’s visual integrity.
- **Data Extraction**: The hidden data can be extracted from the image with ease.
- **User-Friendly Interface**: The project comes with a simple GUI to interact with the system.

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/tapasilikithareddy/Secure-Data-Hiding-in-Image.git
    cd Secure-Data-Hiding-in-Image
    ```

2. **Install Dependencies**
    Install the required libraries using pip:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Project**
    - To hide text in an image, use the `hide_text.py` script.
    - To extract hidden text from an image, use the `extract_text.py` script.

    Example usage:
    ```bash
    python hide_text.py
    python extract_text.py
    ```

## Screenshots
- **Before Image**: The original image without any hidden data.
- **After Image**: The image after hiding the data.

## Conclusion
This project demonstrates how **steganography** can be used to securely hide data within an image. The hidden data remains imperceptible to the human eye, making it a robust solution for secure data communication.

## Future Scope
- **Cryptography Integration**: Integrating encryption methods with steganography to add a layer of protection to the hidden data.
- **Real-Time Data Hiding**: Implementing real-time data embedding and extraction for use in live communication.
- **Larger File Handling**: Optimizing the system to handle larger files and improve image quality.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Python Libraries: Pillow, OpenCV, NumPy
- GitHub: For version control and sharing the code

## Contact
Feel free to reach out for any queries or improvements to the project.
Email: tapasilikithareddy@gmail.com
