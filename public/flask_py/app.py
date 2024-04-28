from flask import Flask, render_template, request, redirect, url_for
import os
import json
import base64
from image_util import allowed_file, parse_image
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder='static')

# Configure a directory to save uploaded files
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def base():
    return render_template('base.html')

@app.route("/word_bank")
def word_bank():
    return render_template('wordbank.html')

@app.route("/wordcard")
def wordcard():
    return render_template('wordcard.html')

@app.route("/aitranslator", defaults={'filename': None})
@app.route("/aitranslator/<filename>")
def aitranslator(filename):
    if filename:
        image_url = url_for('static', filename=f'uploads/{filename}')
    else:
        image_url = None
    return render_template('aitranslator.html', filename=image_url)

#TODO implement template and change
# referencing flask documentation for file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'fileInput' not in request.files:
        print('No file part')
        return redirect(url_for('base'))
    file = request.files.get('fileInput', '')
    if file.filename == '':
        print('No selected file')
        return redirect(url_for('base'))
    if file and allowed_file(file.filename):
        # image_bytes = file.read()
        bytes = base64.b64encode(file.read())
        # get populated dictionary
        image_info = parse_image(bytes)
        image_bytestring = 'data:image/png;base64,' + bytes.decode()
        #TODO use real template link here
        # wordd = [{'text': '．．．', 'translation': '...', 'x': 303, 'y': 0, 'w': 42, 'h': 22, 'romaji': '. . .', 'keywords': [{'phrase': '．．．', 'romaji': '. . .', 'english': '...'}]}, {'text': '・ＣＲ「ｅｘｔｙ', 'translation': "CR 'exty", 'x': 773, 'y': 1, 'w': 93, 'h': 19, 'romaji': "shiiaaru 'ekusutii", 'keywords': [{'phrase': 'ＣＲ', 'romaji': 'shiiaaru', 'english': 'CR'}, {'phrase': 'ｅｘｔｙ', 'romaji': 'ekusutii', 'english': "'exty"}]}, {'text': '．．．ぁぁ、んっ、っ９２１３７６１９これからは、これまでは自分ではないので、', 'translation': 'Ah, mm, 92137619 from now on, up to now it was not me,', 'x': 0, 'y': 20, 'w': 1581, 'h': 72, 'romaji': 'Aa, n, 92137619 kore kara wa, kore made wa jibun de wa nai node,', 'keywords': [{'phrase': 'これからは', 'romaji': 'kore kara wa', 'english': 'from now on'}, {'phrase': 'これまでは', 'romaji': 'kore made wa', 'english': 'up to now'}, {'phrase': '自分ではないので', 'romaji': 'jibun de wa nai node', 'english': 'it was not me'}]}, {'text': '・２０３．１４：７６．１ｈ：２０１', 'translation': '203.14: 76.1h: 201', 'x': 1587, 'y': 69, 'w': 290, 'h': 19, 'romaji': 'Nihyaku-san-ten-ichiyon: Nanajuu-roku-ten-ichi h: Nihyaku-ichi', 'keywords': [{'phrase': '２０３．１４', 'romaji': 'Nihyaku-san-ten-ichiyon', 'english': '203.14'}, {'phrase': '７６．１ｈ', 'romaji': 'Nanajuu-roku-ten-ichi h', 'english': '76.1 hours'}, {'phrase': '２０１', 'romaji': 'Nihyaku-ichi', 'english': '201'}]}]
        # image_info=[{'translation': "私"}, {'translation': "私"}]
        jsoned = json.dumps(image_info, ensure_ascii=False)
        # print(jsoned)
        return render_template('aitranslator.html', 
                              filename=image_bytestring,
                              word_dict=jsoned)    
    else:
        print('Invalid File Type')
        return redirect(url_for('base'))



if __name__ == '__main__':
    app.run(debug=True)
