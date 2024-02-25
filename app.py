from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/result/', methods=['POST'])
def result():
    result_processed = 0
    try:

        equation = request.form['result']

        if "+" in equation:
            arr = equation.split("+", 1)
            result_processed = float(arr[0]) + float(arr[1])
        elif "-" in equation:
            arr = equation.split("-", 1)
            result_processed = float(arr[0]) - float(arr[1])
        elif "*" in equation:
            arr = equation.split("*", 1)
            result_processed = float(arr[0]) * float(arr[1])
        elif "/" in equation:
            arr = equation.split("/", 1)
            result_processed = float(arr[0]) / float(arr[1])

        return render_template('index.html', result=result_processed, success=True)
    except ZeroDivisionError:
        return render_template('index.html', result="Error", error="You cannot divide by zero.", success=False)
    except ValueError:
        return render_template('index.html', result="Error", error="Equation entered not valid.", success=False)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
