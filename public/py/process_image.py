import cv2 as cv2
from comic_text_detector.inference import TextDetector
from manga_ocr import MangaOcr

import PIL.Image as Image
model_path = "comic-text-detector/data/comictextdetector.pt"
max_ratio = 16

def process_image(image_url):
    img = cv2.imread(ls)
    mocr = MangaOcr()

    text_detector = TextDetector(model_path=model_path, input_size=1024, device='cpu', act='leaky')
    mask, mask_refined, blk_list = text_detector(img, refine_mode=1, keep_undetected_mask=True)
    for _, blk in enumerate(blk_list):
      for line_idx, line in enumerate(blk.lines_array()):
          crop_img = blk.get_transformed_region(mask_refined, line_idx, blk.font_size)
          if blk.vertical:
            crop_img = cv2.rotate(crop_img, cv2.ROTATE_90_CLOCKWISE)
          line_text = mocr(Image.fromarray(crop_img))
          print(line_text)

if __name__ == "__main__":
  process_image("test_imgs/better.png")