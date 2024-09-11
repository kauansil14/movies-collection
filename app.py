from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

API_URL = 'http://127.0.0.1:5000/api/movies'

@app.route('/', methods=['GET', 'POST'])
def indx():
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        requests.post(API_URL, json={'title':title, 'genre':genre})
        return redirect('/')
        pass
    response = requests.get(API_URL)
    if response.status_code == 200:
            movies = response.json()
    else:
            movies = []
    return render_template('index.html', movies=movies)

@app.route('/delete/<int:id>')
def delete(id):
    requests.delete(f'{API_URL}/{id}')
    return redirect('/')

@app.route('/update/<int:id>')
def update(id):
    if request.method =='POST':
        title = request.get['title']
        genre = request.get['genre']
        requests.put(f'{API_URL}/{id},json={'title' title, 'genre': genre}')



        return redirect('/')
    
    response = requests.get(f'{API_URL}/{id}')
    if response.status_code == 200:
        movie = response.json()
    else:
        movie = {}

    return render_template('update.html', movie)

if __name__ == '__main__':
    app.run(port=5001, debug=True)