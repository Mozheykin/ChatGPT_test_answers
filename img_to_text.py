from pprint import pprint
from PIL import Image
import cv2
import pytesseract
import numpy
import re

def img_to_text(img:Image, split_chars:list, split_symbols:list, max_h:int = 31, max_w:int = 31) -> list:
    result = list()
    img = numpy.array(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255,  cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    # thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            # cv2.THRESH_BINARY_INV,11,2)
    dict_result = pytesseract.image_to_data(thresh, output_type=pytesseract.Output.DICT)
    position_char_answer = list()
    position_symbol_answer = list()
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
            splits_symbols = [split_char in value for split_char in split_symbols]
            splits_chars = re.search(r'(\s|O)[A-Z]\.', value)             
            thresh = cv2.rectangle(thresh, (x, y), (x + w, y + h), (0, 255, 0), 3)
            if splits_chars is not None:
                position_char_answer.append({
                                            'x': x, 
                                            'y': y, 
                                            'w': w, 
                                            'h': h,
                                        })
            if all([any(splits_symbols), h in [w+ind for ind in range(-1, 2)]]):
                position_symbol_answer.append({
                                            'x': x, 
                                            'y': y, 
                                            'w': w, 
                                            'h': h,
                                        })

    # cv2.imshow("ROI", thresh)
    # cv2.waitKey(15000)
    # cv2.destroyAllWindows()
    print(position_char_answer)
    print(position_symbol_answer)
    pprint(result)
    if len(position_char_answer) > 2:
        return result, position_char_answer
    if len(position_symbol_answer) > 2:
        return result, position_symbol_answer

    return None, None
