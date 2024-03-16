from flask import Flask, render_template, request, jsonify
import numpy as np
import math 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        Ptot = float(request.form['Ptot'])
        Pstat = float(request.form['Pstat'])
        operation = request.form['gas']
        
        if operation == 'Air':
            gamma = 1.4
            mwt = 29
        elif operation == 'Nitrogen':
            gamma = 1.4
            mwt = 28
        elif operation == 'Oxygen':
            gamma = 1.4
            mwt = 16
        elif operation == 'Carbon Dioxide':
            gamma = 1.28
            mwt = 44
        mach = math.sqrt(2/(gamma-1)*((Ptot/Pstat)**((gamma-1)/gamma)-1))
        result = mach
        return jsonify({'result': np.round(result,4)})

if __name__ == '__main__':
    app.run(debug=True)