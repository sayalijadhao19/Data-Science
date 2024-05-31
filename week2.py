from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calculator</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .calculator-container {
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                width: 300px;
                text-align: center;
            }
            .calculator-container h1 {
                color: #333;
                margin-bottom: 20px;
            }
            .calculator-container label {
                display: block;
                margin-bottom: 10px;
                color: #555;
            }
            .calculator-container input[type="number"],
            .calculator-container select {
                width: 100%;
                padding: 10px;
                margin-bottom: 20px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            .calculator-container input[type="submit"] {
                width: 100%;
                padding: 10px;
                background-color: #28a745;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 16px;
            }
            .calculator-container input[type="submit"]:hover {
                background-color: #218838;
            }
            .result {
                margin-top: 20px;
                font-size: 18px;
                color: #333;
            }
        </style>
    </head>
    <body>
        <div class="calculator-container">
            <h1>Simple Calculator</h1>
            <form method="POST" action="/calculate">
                <label for="n1">Enter first number:</label>
                <input type="number" id="n1" name="n1" required>
                <label for="n2">Enter second number:</label>
                <input type="number" id="n2" name="n2" required>
                <label for="opr">Select an operator:</label>
                <select name="opr" id="opr" required>
                    <option value="add">+</option>
                    <option value="sub">-</option>
                    <option value="mul">*</option>
                    <option value="div">/</option>
                </select>
                <input type="submit" value="Calculate">
            </form>
            {% if result is not none %}
                <div class="result">
                    Result: {{ result }}
                </div>
            {% endif %}
        </div>
    </body>
    </html>
    """)

@app.route("/calculate", methods=["POST"])
def calculate():
    n1 = int(request.form['n1'])
    n2 = int(request.form['n2'])
    oper = request.form['opr']
    result = 0
    if oper == "add":
        result = n1 + n2
    elif oper == "sub":
        result = n1 - n2
    elif oper == "mul":
        result = n1 * n2
    elif oper == "div":
        result = n1 / n2
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calculator</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .calculator-container {
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                width: 300px;
                text-align: center;
            }
            .calculator-container h1 {
                color: #333;
                margin-bottom: 20px;
            }
            .calculator-container label {
                display: block;
                margin-bottom: 10px;
                color: #555;
            }
            .calculator-container input[type="number"],
            .calculator-container select {
                width: 100%;
                padding: 10px;
                margin-bottom: 20px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            .calculator-container input[type="submit"] {
                width: 100%;
                padding: 10px;
                background-color: #28a745;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 16px;
            }
            .calculator-container input[type="submit"]:hover {
                background-color: #218838;
            }
            .result {
                margin-top: 20px;
                font-size: 18px;
                color: #333;
            }
        </style>
    </head>
    <body>
        <div class="calculator-container">
            <h1>Simple Calculator</h1>
            <form method="POST" action="/calculate">
                <label for="n1">Enter first number:</label>
                <input type="number" id="n1" name="n1" required>
                <label for="n2">Enter second number:</label>
                <input type="number" id="n2" name="n2" required>
                <label for="opr">Select an operator:</label>
                <select name="opr" id="opr" required>
                    <option value="add">+</option>
                    <option value="sub">-</option>
                    <option value="mul">*</option>
                    <option value="div">/</option>
                </select>
                <input type="submit" value="Calculate">
            </form>
            <div class="result">
                Result: {{ result }}
            </div>
        </div>
    </body>
    </html>
    """, result=result)

if __name__ == '__main__':
    app.run(debug=True, port=7007)
