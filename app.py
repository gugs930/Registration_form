from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('registration.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    city = request.form['city']
    return render_template('confirm.html', name=name, age=age, city=city)

if __name__ == '__main__':
    app.run(debug=True)
