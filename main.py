from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    favicon_path = os.path.join(app.root_path, 'static', 'images', 'favicon.png')
    return send_file(favicon_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)

