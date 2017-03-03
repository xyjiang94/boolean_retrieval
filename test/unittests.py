# -*- coding: utf-8 -*-
import unittest
#from xy import *
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from boolean_index import import_dict
from process_text import process_text


def test_dict():
    movie_dict2 = import_dict("test/test_corpus.json")
    dict1 = {1:"a"}
    assert type(movie_dict2) == type(dict1)


def test_nltk():
    movie_dict = import_dict("test/test_corpus.json")
    text = movie_dict["1"]["text"]
    stop_list = ['and', 'into', 'it', 'an', 'as', 'are', 'in', 'its', 'from', 'to', 'had', 'same', 'their', 'between', 'has', 'until', 'his', 'who', 'with', 'by', 'is', 'a', 'on', 'these', 'of', 'no', 'this', 'the', 'at']
    l1,l2 = process_text(text)
    assert l2 == stop_list

def test_stem():
    l1,l2 = process_text("sentences")
    assert l1[0] == "sentenc"
    l1,l2 = process_text("happiness")
    assert l1[0] == "happi"

def test_stopword():
    l1,l2 = process_text("is apple")
    assert l1[0] == "appl"
    assert l2[0] == "is"

def test_equivalent():
    l1,l2 = process_text("running")
    l3,l4 = process_text("run")
    assert l3[0] == l1[0]
    
# nosetests xxx.py
