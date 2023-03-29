from PIL import Image
import cv2
import pytesseract
import numpy

def img_to_text(img:Image) -> list:
    result = list()
    img = numpy.array(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    
    dict_result = pytesseract.image_to_data(thresh, output_type=pytesseract.Output.DICT)
    for index, value in enumerate(dict_result['text']):
        if value:
            x = dict_result.get('left')[index] 
            y = dict_result.get('top')[index] 
            w = dict_result.get('width')[index] 
            h = dict_result.get('height')[index]
            result.append(
                {
                'x': x, 
                'y': y, 
                'w': w, 
                'h': h, 
                'text': value,
                }
            )
            if "©" in value:
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)


    # cv2.imshow("ROI", img)
    # cv2.waitKey(15000)
    # cv2.destroyAllWindows()
    
    return result
