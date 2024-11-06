import os
import numpy as np
from PIL import Image
from collections import Counter
import math

def calculate_image_entropy(image_path):
    """Calculate the entropy of an image file."""
    # Open image and convert to grayscale
    image = Image.open(image_path).convert('L')
    
    # Get the histogram of the image
    histogram = image.histogram()
    
    # Normalize the histogram
    histogram = np.array(histogram) / sum(histogram)
    
    # Calculate the entropy
    entropy = -np.sum([p * np.log2(p) for p in histogram if p != 0])
    
    return entropy

def calculate_binary_entropy(bin_path):
    """Calculate the entropy of a binary file."""
    with open(bin_path, "rb") as file:
        binary_data = file.read()
    
    # Count the occurrences of each byte value (0-255)
    byte_counts = Counter(binary_data)
    total_bytes = len(binary_data)
    
    # Calculate entropy
    entropy = -sum((count / total_bytes) * math.log2(count / total_bytes) for count in byte_counts.values())
    
    return entropy

def calculate_entropy(file_path):
    """Determine the file type and calculate entropy accordingly."""
    if file_path.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
        print("Processing as an image file.")
        return calculate_image_entropy(file_path)
    else:
        print("Processing as a binary file.")
        return calculate_binary_entropy(file_path)

# Example usage:
file_path = "1_1.jpg.xyt"
# Replace with the path to your file (image or .bin)

# Check if the file exists before attempting to open it
if os.path.exists(file_path):
    entropy_value = calculate_entropy(file_path)
    print(f"Entropy of the file: {entropy_value} bits")
else:
    print("File does not exist at the specified path.")
