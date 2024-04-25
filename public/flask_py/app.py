from flask import Flask, render_template, request, redirect, url_for
import os
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

@app.route("/upload", methods=['POST'])
def upload_file():
    if 'fileInput' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['fileInput']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return redirect(url_for('aitranslator', filename=filename))

if __name__ == '__main__':
    app.run(debug=True)
