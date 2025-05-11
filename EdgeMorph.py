import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename
import tkinter as tk

# Get image path via file dialog
root = tk.Tk()
root.withdraw()
image_path = askopenfilename(title="Select image", filetypes=[("Images", "*.jpg *.png *.jpeg *.bmp")])
if not image_path:
    print("No image selected.")
    exit()

# Load image
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if img is None:
    print("Error loading image.")
    exit()

# Resize, Rotate, Translate
resized = cv2.resize(img, (300, 300))
h, w = resized.shape[:2]
rotated_translated = cv2.warpAffine(resized, cv2.getRotationMatrix2D((w // 2, h // 2), 30, 1), (w, h))
rotated_translated = cv2.warpAffine(rotated_translated, np.float32([[1, 0, 30], [0, 1, 20]]), (w, h))

# Edge detect, morph ops
edges = cv2.Canny(cv2.GaussianBlur(rotated_translated, (5, 5), 0), 50, 150)
kernel = np.ones((5, 5), np.uint8)
dilated = cv2.dilate(edges, kernel, iterations=1)
eroded = cv2.erode(dilated, kernel, iterations=1)
gradient = cv2.morphologyEx(rotated_translated, cv2.MORPH_GRADIENT, kernel)

# Display
titles = ['Original', 'Transformed', 'Edges', 'Dilated', 'Eroded', 'Gradient']
images = [img, rotated_translated, edges, dilated, eroded, gradient]

plt.figure(figsize=(10, 6))
for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
