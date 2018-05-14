from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        return render_template('index.html')
    else:
        return render_template('add_item.html')

if __name__ == '__main__':
    app.run()