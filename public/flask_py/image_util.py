from image_to_ds import text_ocr_to_dictionary, populate_translation_keywords

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def parse_image(image_bytes):
    
    # convert into base64 np array for process_image
    d = text_ocr_to_dictionary(image_bytes)
    print("populating translation...")
    d = populate_translation_keywords(d)
    print(d)
    return d
    # return img
