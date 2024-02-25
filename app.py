from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """ Displays the index page accessible at '/' """
    return render_template('index.html')


@app.route('/result/', methods=['POST'])
def result():
    return render_template, 'index.html'


if __name__ == '__main__':
    app.run(port=8000, debug=True)
