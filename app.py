# -*- coding: utf-8 -*-
from flask import *
from flask import Flask, session
from flask.ext.session import Session
from boolean_query import final_search
#import json
import random, string


app = Flask(__name__)
SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)
#app.secret_key = 'any random string'

@app.route("/")
def searchbox():
    return render_template('search_box.html')


@app.route("/search_results", defaults={'page': 1}, methods=['POST','GET'])
@app.route("/search_results/<page>", methods=['POST','GET'])
def search_results(page):
    if request.method == 'POST':
        query = request.form['query']
        dire = request.form['dire']
        star = request.form['star']
        loc = request.form['loc']
        results,stops = final_search(query,dire,star,loc)
        session['results'] = results
        session['stops'] = stops
    else:
        results = session['results']
        stops = session['stops']

    total = int(len(results)/10)
    page = int(page)
    print page
    results_part = results[0 + (page-1)*10 : 10 + (page-1)*10]

    if len(results) > 0:
        return render_template('search_result.html', results = results_part, stops = stops, total = total, page = page)
    else:
        return render_template('search_empty.html')


@app.route('/doc/<num>')
def display_doc(num):
    json_path = "2016_movies_standard.json"
    movie_file = open(json_path, 'r')
    movie_dict = json.loads(movie_file.read())
    doc = movie_dict[str(num)]
    print doc
    return render_template('doc.html',movie = doc)

@app.route('/set')
def set():
    session['username'] = ''.join(random.choice(string.lowercase) for i in range(5))
    #session['username'] = [1,2,3]
    return "set successful"

@app.route('/check')
def check():
    if 'username' in session:
        s
        return session['username']+"in session"
    else:
        return "GG"


if __name__ == "__main__":
    app.run(debug = 'True')
