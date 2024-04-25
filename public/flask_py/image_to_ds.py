# import sys
# sys.path.append('/.venv/lib/python3.9/site-packages')
import cv2 as cv2
import numpy as np
import base64
from comic_text_detector.inference import TextDetector
from manga_ocr import MangaOcr

import PIL.Image as Image
model_path = "model/comictextdetector.pt"
max_ratio = 16


# input: image as base64 np array
# output: list of dictionaries
# each dictionary entry is formatted as {text: raw_text, x: x_coord, y: y_coord, w: width, h: height, translation: translated_text, keywords: [list of keywords]}
def text_ocr_to_dictionary(image_bytes):
  # given a bytestring, convert to np, then decode into cv2 format
  img_as_np = np.frombuffer(base64.b64decode(image_bytes), np.uint8)
  img = cv2.imdecode(img_as_np, cv2.IMREAD_COLOR)
  mocr = MangaOcr()

  text_detector = TextDetector(model_path=model_path, input_size=1024, device='cpu', act='leaky')
  _, mask_refined, blk_list = text_detector(img, refine_mode=1, keep_undetected_mask=True)
  text_info = []

  for _, blk in enumerate(blk_list):
    line_text = ""
    x,y,w,h = blk.xywh()
    for line_idx, _ in enumerate(blk.lines_array()):
        crop_img = blk.get_transformed_region(mask_refined, line_idx, blk.font_size)
        if blk.vertical:
          crop_img = cv2.rotate(crop_img, cv2.ROTATE_90_CLOCKWISE)
        line_text += mocr(Image.fromarray(crop_img))
    if line_text:
      text_info.append(
        {
          'text': line_text,
          'translation': '',
          'x': x,
          'y': y,
          'w': w,
          'h': h,
          'keywords': []
        }
      )
  print(text_info)
  return text_info

# populate the translation and keywords fields in text_info
# input: text_info is a list of dictionaries, see text_ocr_to_dictionary() comment for information
# output: none; populate text_info in place
def populate_translation_keywords(text_info):
  #TODO
  #YUHAN CODE HERE
  return

# testing only, remove later
if __name__ == "__main__":
  image = cv2.imencode(cv2.imread("test_imgs/better.png"))
  text_ocr_to_dictionary(image)