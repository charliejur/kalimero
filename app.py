# app.py

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def calculator():
  return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
  num1 = float(request.form['num1'])
  num2 = float(request.form['num2'])
  operation = request.form['operation']

  if operation == 'add':
    result = num1 + num2
  elif operation == 'subtract':
    result = num1 - num2
  elif operation == 'multiply':
    result = num1 * num2
  elif operation == 'divide':
    result = num1 / num2

  return render_template('calculator.html', result=result)

if __name__ == '__main__':
  app.run()
