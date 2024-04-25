import base64
from image_to_ds import text_ocr_to_dictionary

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def parse_image(image):
    image_bytes = base64.b64encode(image.read())
    # convert into base64 np array for process_image
    return text_ocr_to_dictionary(image_bytes)
    # return img
