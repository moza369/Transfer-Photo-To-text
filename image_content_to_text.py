import pytesseract
import sys
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'


def image_to_text(image_path):
    try:
        with Image.open(image_path) as img:
            text = pytesseract.image_to_string(img)
            return text
            
    except Exception as e:
        print("An error occurred:", e)
        return None


image_path = sys.argv[1]  
text = image_to_text(image_path)
if text:
    print("Extracted text: \n")
    print(text)
else:
    print("Failed to extract text from the image.")
