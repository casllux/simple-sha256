from flask import Flask, render_template, request

from code import hash_value

app = Flask(__name__)

@app.route('/')
def get_ui():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def calculate_hash():
    
    data = request.form.get('data')
    hashed = hash_value(data)

    return render_template('index.html', hash=hashed,value=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)