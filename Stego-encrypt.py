import cv2
import os

# Load image
image_path = "Flower.jpg"  # Replace with actual image
img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found!")
    exit()

# Get user input
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Convert message to ASCII values
d = {chr(i): i for i in range(255)}
h, w, _ = img.shape  # Get image dimensions

# Check if message fits in the image
if len(msg) > h * w:
    print("Error: Message too long for this image!")
    exit()

# Encode message into the Blue channel
index = 0
for i in range(h):
    for j in range(w):
        if index < len(msg):
            img[i, j, 0] = d[msg[index]]  # Modify blue channel
            index += 1
        else:
            break

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)
print("Message hidden successfully in 'encryptedImage.jpg'!")
