# 🖼️ Image Processing with OpenCV

This Python script performs basic image processing operations using OpenCV. It allows a user to select an image through a file dialog and applies a series of transformations and morphological operations, displaying the results using `matplotlib`.

## 🔧 Features

* Load grayscale image using a file dialog (`tkinter`)
* Resize, rotate, and translate the image
* Apply Gaussian blur and Canny edge detection
* Perform dilation, erosion, and morphological gradient
* Display all stages in a single matplotlib window

## 📦 Requirements

* Python 3.x
* OpenCV (`cv2`)
* NumPy
* Matplotlib
* Tkinter (comes with standard Python installation)

Install dependencies (if needed):

```bash
pip install opencv-python numpy matplotlib
```

## ▶️ How to Run

```bash
python image_processing.py
```

* A file dialog will appear—choose a grayscale-compatible image (`.jpg`, `.png`, `.jpeg`, `.bmp`).
* The script will display six processed images in a 2x3 grid:

  1. Original
  2. Transformed (resized, rotated, translated)
  3. Edges (Canny)
  4. Dilated
  5. Eroded
  6. Morphological Gradient

## 📁 Example Output

![Example](path/to/sample_output.png) <!-- Replace with actual image path if hosting screenshots -->

## 📝 Notes

* The image is converted to grayscale during loading.
* Adjust kernel sizes and parameters in the script to experiment with different effects.


