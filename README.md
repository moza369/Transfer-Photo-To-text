# Transfer-Photo-To-text
python script transfer  photo content to text

# Install requirement
sudo apt-get update
sudo apt-get install tesseract-ocr
# Install Python lib
pip install pytesseract pillow

# Edit The script
when the installation of tesseract finish
you need to change the path of tessercat in the script 
you can use cmd : which tessercat
and copy the PATH then put it in line 4 pytesseract.pytesseract.tesseract_cmd = r'PATH'

# How to use the script
python3 file_name.py path_to_photo
