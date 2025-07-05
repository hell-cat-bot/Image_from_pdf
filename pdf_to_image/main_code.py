import cv2
import matplotlib.pyplot as plt
from rectangle import Rectangle
import os
import numpy as np
from PIL import Image
from pdf2image import convert_from_path  # Convert PDF to images
from helpers import *

# Define input PDF path
pdf_path = r"C:\Users\pc\Downloads\Telegram Desktop\[ME] [039] Maybe Meant to Be [@Manga_Edge].pdf"

# Define output folder
output_folder = r"C:\Users\pc\Downloads\pythooo\images\final\c39"
os.makedirs(output_folder, exist_ok=True)  # Ensure output folder exists

# Convert PDF to images
images = convert_from_path(pdf_path)

for page_num, pil_img in enumerate(images):
    # Convert PIL image to OpenCV format
    img = np.array(pil_img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    # Get contours from the image
    contours = get_contours(img)
    filtered_contours = remove_specks_and_lines(img, contours)
    crops = get_crops(img, filtered_contours)
    crops = remove_small_crops(img, crops)
    crops = merge_overlapping_crops(crops)
    
    # Save each cropped image
    for i, crop in enumerate(crops):
        cropped_image = img[crop.y:crop.z, crop.x:crop.w, :]
        output_path = os.path.join(output_folder, f"page_{page_num+1}_crop_{i+1}.jpg")
        cv2.imwrite(output_path, cropped_image)
        print(f"✅ Saved: {output_path}")
        
        # Display the cropped image
        #plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
        #plt.show()
