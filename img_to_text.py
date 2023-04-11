from PIL import Image
import cv2
import pytesseract
import numpy
import re

def img_to_text(img:Image, split_chars:list, split_symbols:list, max_h:int = 20, max_w:int = 20) -> list:
    result = list()
    position_answers = list()
    img = numpy.array(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    
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
            # splits = [split_char in value for split_char in split]

            # splits_chars = [split_char in value for split_char in split_chars]
            splits_symbols = [split_char in value for split_char in split_symbols]
            splits_chars = re.search(r'[A-Z]\.', value)             
            if all([h in [w+ind for ind in range(-5, 5)], h <= max_h, w <= max_w]):
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                if splits_chars:
                    position_char_answer.append({
                                                'x': x, 
                                                'y': y, 
                                                'w': w, 
                                                'h': h,
                                            })
                if any([splits_symbols]):
                    position_symbol_answer.append({
                                                'x': x, 
                                                'y': y, 
                                                'w': w, 
                                                'h': h,
                                            })

    # cv2.imshow("ROI", img)
    # cv2.waitKey(15000)
    # cv2.destroyAllWindows()
    if len(position_symbol_answer) > 2:
        return result, position_symbol_answer
    if len(position_char_answer) > 2:
        return result, position_char_answer
