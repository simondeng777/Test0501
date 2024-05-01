import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"c:\Program Files\Tesseract-OCR\tesseract.exe"
img = Image.open(r"word.jpg")
#img.show()
print(pytesseract.image_to_string(img, lang="eng"))