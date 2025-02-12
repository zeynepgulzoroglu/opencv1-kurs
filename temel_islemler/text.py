from PIL import Image
import pytesseract

img = Image.open(r"C:\Users\zeyne\Desktop\opencvkurs\temel_islemler\text.png")
text = pytesseract.image_to_string(img,lang="eng")
print(text)