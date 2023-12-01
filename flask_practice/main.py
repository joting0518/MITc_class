from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        greeting = f"Hello, {name}!"
        return render_template('index.html', greeting=greeting)
    return render_template('index.html', greeting=None)

if __name__ == '__main__':
    app.run(debug=True)
