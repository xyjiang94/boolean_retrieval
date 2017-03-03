# -*- coding: utf-8 -*-
import json
import shelve
import process_text
from index import Index

def import_dict (path):
    movie_file = open(path, 'r')
    movie_dict = json.loads(movie_file.read())
    return movie_dict

def store (k, terms, shlf_path):
    main_shlv =  shelve.open(shlf_path, 'c')
    for w in terms:
        if w in main_shlv:
            index = main_shlv[w]
        else:
            index = Index()
        index.add_doc(int(k))
        main_shlv[w] = index
    main_shlv.close()


json_path = "2016_movies_standard.json"
movie_dict = import_dict(json_path)

for (k,movie) in  movie_dict.items():

    title = movie["title"]
    text = movie["text"]
    director = movie['director']
    starring = movie['starring']
    location = movie['location']

    terms,l = process_text.process_text(title+text)
    dire,l = process_text.process_text(director)
    star,l = process_text.process_text(starring)
    loc,l = process_text.process_text(location)

    store(k, terms, "./db/main_index")
    store(k, dire, "./db/dir_index")
    store(k, star, "./db/star_index")
    store(k, loc, "./db/loc_index")
