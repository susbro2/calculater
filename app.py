from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        operation = request.form['operation']
        
        if operation == 'sqrt':
            num1 = float(request.form['num1'])
            result = f"√{num1} = {math.sqrt(num1):.2f}"
        else:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            
            if operation == 'add':
                result = f"{num1} + {num2} = {num1 + num2}"
            elif operation == 'subtract':
                result = f"{num1} - {num2} = {num1 - num2}"
            elif operation == 'multiply':
                result = f"{num1} * {num2} = {num1 * num2}"
            elif operation == 'divide':
                if num2 == 0:
                    result = "❌ Error: Cannot divide by zero!"
                else:
                    result = f"{num1} / {num2} = {num1 / num2:.2f}"
            elif operation == 'power':
                result = f"{num1} ^ {num2} = {num1 ** num2}"
            elif operation == 'percentage':
                result = f"{num1}% of {num2} = {(num1 * num2) / 100:.2f}"
            elif operation == 'modulus':
                if num2 == 0:
                    result = "❌ Error: Cannot divide by zero!"
                else:
                    result = f"{num1} mod {num2} = {num1 % num2}"
    
    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)