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
you can use cmd : # which tessercat  #
and copy the PATH then put it in line 4 pytesseract.pytesseract.tesseract_cmd = r'PATH'

# How to use the script
python3 file_name.py path_to_photo

# example
![endomorph](https://github.com/moza369/Transfer-Photo-To-text/assets/71130647/328ea663-d6b8-43f9-ac5a-d4a55f6f4b0f)

Extracted text: 

La réduction d’endomorphisme a pour objectif d’exprimer des matrices et des
endomorphismes sous une forme plus simple, par exemple pour faciliter les calculs.
Cela consiste essentiellement & trouver une décomposition de l’espace vectoriel un
somme directe de sous espaces stables sur lesquels l’endomorphisme induit est plus
simple. Moins géométriquement, cela correspond a trouver une base de l’espace dans
laquelle l’endomorphisme s’exprime simplement.

Dans toute la suite de ce chapitre, K = R ou C et E est désigne un K-espace vectoriel
de dimension finie n € N non réduit (0), et f un endomorphisme de E.



