
from flask import Flask, flash, request, redirect, render_template, url_for
from image_util import allowed_file, parse_image

app = Flask(__name__)

# 
# ========
# ENDPOINTS
# ========
# 

@app.route("/")
def index():
    return render_template('index.html')

#TODO
# THIS IS A DUMMY FOR ADDING VARIABLES TO A TEMPLATE
@app.route("/translator")
def dummy():
    return render_template('hello.html', name="this is the name")

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

#TODO implement word list visualization
@app.route("/wordlist")
def word_list():
    return render_template('FIXME.html', words=[])

if __name__ == '__main__':
    
    app.debug = True
    app.run()