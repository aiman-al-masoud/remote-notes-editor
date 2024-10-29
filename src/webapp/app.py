from flask import Flask, render_template, request

app = Flask(__name__)
FILE = ''
TEXT = ''


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/get-text', methods=['GET', 'POST'])
def get_text():
    return TEXT

@app.route('/set-text', methods=['GET', 'POST'])
def set_text():

    global TEXT

    if request.json:
        TEXT = request.json['text']

    return 'ok'

@app.route('/set-filepath', methods=['GET', 'POST'])
def set_filepath():

    global FILE

    if request.json:
        FILE = request.json['filepath']

    return 'ok'

@app.route('/get-filepath', methods=['GET', 'POST'])
def get_filepath():
    return FILE

# app.run()
