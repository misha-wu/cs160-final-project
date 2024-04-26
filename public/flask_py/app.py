from flask import Flask, render_template, request, redirect, url_for
import os
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
    if 'image' not in request.files:
        flash('No file part')
        return redirect(url_for('/'))
    file = request.files['image']
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('/'))
    if file and allowed_file(file.filename):
        image = request.files['image']  
        
        # get populated dictionary
        image_info = parse_image(image)

        #TODO use real template link here
        return render_template('FIXME.html', image_info=image_info)    
    else:
        flash('Invalid File Type')
        return redirect(url_for('/'))

if __name__ == '__main__':
    app.run(debug=True)
