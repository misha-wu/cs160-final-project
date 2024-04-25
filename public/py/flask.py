from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data')
def send_data():
    # Example data
    data = {'message': 'Hello from Python!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

