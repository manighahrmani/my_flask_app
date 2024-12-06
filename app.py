from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get data from the form
    name = request.form['name']
    return f"Hello, {name}! Welcome to your interactive Flask app!"

if __name__ == '__main__':
    app.run(debug=True)
