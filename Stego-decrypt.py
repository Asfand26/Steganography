import cv2
import os

# Load encrypted image
image_path = "encryptedImage.jpg"
img = cv2.imread(image_path)

if img is None:
    print("Error: Encrypted image not found!")
    exit()

# Get passcode
pas = input("Enter passcode for decryption: ")

# Ask for the same passcode used during encryption
password = input("Re-enter the passcode used during encryption: ")

if password != pas:
    print("YOU ARE NOT AUTHORIZED!")
    exit()

# Create decoding dictionary
c = {i: chr(i) for i in range(256)}  # Ensures full ASCII range

h, w, _ = img.shape  # Get image dimensions

message = ""
n, m, z = 0, 0, 0  # Start positions

for _ in range(h * w):  # Avoid out-of-bounds error
    pixel_value = img[n, m, z]  # Extract blue channel value
    
    if pixel_value not in c:
        break  # Stop if we hit an invalid value

    char = c[pixel_value]  # Convert pixel value to character
    
    if char == "\x00":  # Stop at null terminator
        break

    message += char

    # Update indices to match encryption logic
    n = (n + 1) % h
    m = (m + 1) % w
    z = (z + 1) % 3  # Cycle through RGB channels

print("Decrypted Message:", message)
