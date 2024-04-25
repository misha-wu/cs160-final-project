from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route("/")
def base():
    return render_template('base.html')

@app.route("/word_bank")
def word_bank():
    return render_template('wordbank.html')


if __name__ == '__main__':
    app.run(debug=True)
