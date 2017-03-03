# -*- coding: utf-8 -*-
import json
import shelve
from process_text import process_text
from index import Index
import sys

def intersect(l1,l2):
    i = 0
    j = 0
    l = []
    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:
            l.append(l1[i])
            i += 1
            j += 1
        elif l1[i] < l2[j]:
            while i < len(l1) and l1[i] < l2[j]:
                i += 1
        else:
            while j < len(l2) and l1[i] > l2[j]:
                j += 1
    return l

def get_doc_abstarct(doc_nums):
    json_path = "2016_movies_standard.json"
    movie_file = open(json_path, 'r')
    movie_dict = json.loads(movie_file.read())
    results = []
    for num in doc_nums:
        d = {}
        d["num"] = num
        d["director"] = movie_dict[str(num)]['director']
        d["starring"] = movie_dict[str(num)]['starring']
        d["location"] = movie_dict[str(num)]['location']
        d["title"] = movie_dict[str(num)]['title']
        d["text"] = movie_dict[str(num)]['text'][0:200]
        results.append(d)
    return results

def get_index(terms,shlf_path):
    term_index = shelve.open(shlf_path, 'c')
    min_len = sys.maxint
    min_number = 0
    i = 0
    index_list = []
    for term in terms:
        if term not in term_index.keys():
            return [],[]
        else:
            index = term_index[term]
            index_list.append(index.docs)
            if index.len < min_len:
                min_number = i
                min_len = index.len
    return index_list,min_number

def query_search(query,keyword):
    path_dict = {
        "main":"./db/main_index.db",
        "dir":"./db/dir_index.db",
        "star":"./db/star_index.db",
        "loc":"./db/loc_index.db",
    }

    shlf_path = path_dict[keyword]
    #term_index = shelve.open(shlf_path, 'c')

    terms,stops = process_text(query)
    if len(terms) == 0:
        return [],stops


    index_list,min_number = get_index(terms,shlf_path)

    return index_list,stops
    # doc_nums = index_list[min_number]
    # for l in index_list:
    #    doc_nums = intersect(doc_nums,l)
    #
    # return get_doc_abstarct(doc_nums),stops


def final_search(query,dire,star,loc):
    l_q,stops = query_search(query,"main")
    l_d,l= query_search(dire,"dir")
    l_s,l = query_search(star,"star")
    l_l,l = query_search(loc,"loc")

    index_list = l_q + l_d + l_s +l_l
    if len(index_list) == 0:
        return [],stops
    min_len = sys.maxint
    min_number = 0
    i = 0
    for l in index_list:
        if len(l) < min_len:
            min_number = i
            min_len = len(l)
        i += 1
    doc_nums = index_list[min_number]
    for l in index_list:
       doc_nums = intersect(doc_nums,l)

    return get_doc_abstarct(doc_nums),stops


#l1,l2 =  final_search("sofi","","","")
#print l1
