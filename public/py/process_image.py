import cv2 as cv2
from comic_text_detector.inference import TextDetector
from manga_ocr import MangaOcr

import PIL.Image as Image
model_path = "model/comictextdetector.pt"
max_ratio = 16

def process_image(image_url):
  # todo: can we replace this with base64?
  img = cv2.imread(image_url)
  mocr = MangaOcr()

  text_detector = TextDetector(model_path=model_path, input_size=1024, device='cpu', act='leaky')
  _, mask_refined, blk_list = text_detector(img, refine_mode=1, keep_undetected_mask=True)
  text_blocks_and_loc = []

  for _, blk in enumerate(blk_list):
    line_text = ""
    x,y,w,h = blk.xywh()
    for line_idx, _ in enumerate(blk.lines_array()):
        crop_img = blk.get_transformed_region(mask_refined, line_idx, blk.font_size)
        if blk.vertical:
          crop_img = cv2.rotate(crop_img, cv2.ROTATE_90_CLOCKWISE)
        line_text += mocr(Image.fromarray(crop_img))
    
    if line_text:
      text_blocks_and_loc.append({"text": line_text, "x": x, "y": y, "w": w, "h": h})
  print(text_blocks_and_loc)
  return text_blocks_and_loc

if __name__ == "__main__":
  process_image("test_imgs/better.png")