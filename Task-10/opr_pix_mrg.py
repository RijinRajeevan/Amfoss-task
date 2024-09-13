import os
import cv2
from PIL import Image, ImageDraw
assets_path = "/home/rijin-rajeevan/amFOSS/Task 10/ OperationPixelMerge/assets"
def extract_number(filename):
    parts = filename.split('.')
    number_part = ''.join([char for char in parts[0] if char.isdigit()])
    return int(number_part) if number_part else float('inf')

image_filenames = sorted(os.listdir(assets_path), key=extract_number)
coordinates = []
colors = []

for filename in image_filenames:
    image_path = os.path.join(assets_path, filename)
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh_image = cv2.threshold(gray_image, 250, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(largest_contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            color = image[cY, cX].tolist()
            coordinates.append((cX, cY))
            colors.append(tuple(color[::-1])) 
    else:
        coordinates.append(None)
        colors.append(None)
output_image = Image.new('RGB', (512, 512), 'white')
draw = ImageDraw.Draw(output_image)
for i in range(len(coordinates) - 1):
    if coordinates[i] is not None and coordinates[i + 1] is not None:
        draw.line([coordinates[i], coordinates[i + 1]], fill=colors[i], width=2)

output_image.save('stitched_output.png')
