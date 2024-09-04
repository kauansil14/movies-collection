from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = 'http://127.0.0.1:5000/api/movies'

@app.route('/', methods=['GET'])
def indx():
    response = requests.get(API_URL)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5001, debug=True)