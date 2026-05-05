from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('index.html')   # serves file from root

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    num1 = float(data['num1'])
    num2 = float(data['num2'])
    operator = data['operator']

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = "Cannot divide by zero" if num2 == 0 else num1 / num2
    else:
        result = "Invalid operator"

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)