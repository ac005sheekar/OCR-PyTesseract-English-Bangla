from PIL import Image
import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

img = cv2.imread('sbanerjee.PNG')
tex = pytesseract.image_to_string(Image.open('sbanerjee.PNG'), lang='ben')
print("The Bangla Output is:     ", pytesseract.image_to_string(Image.open('sbanerjee.PNG'), lang='ben'))

cv2.namedWindow("Sheekar OCR")
cv2.imshow("Input Image", img)

cv2.waitKey(0)

cv2.destroyWindow("Test")
cv2.destroyWindow("Main")

