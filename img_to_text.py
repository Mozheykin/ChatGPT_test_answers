from PIL import Image
import cv2
import pytesseract
import numpy

def img_to_text(img:Image) -> list:
    result = list()
    img = numpy.array(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    contours, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        roi = img[y:y+h, x:x+w]
        text = pytesseract.image_to_string(roi)
        if 'Question' in text:
            result.append({'x': x, 'y': y, 'w': w, 'h': h, 'text': text.strip()})
    
    cv2.imshow("Image", img)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()
    
    return result
