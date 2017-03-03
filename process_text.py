import nltk
from nltk.corpus import stopwords
import string

def process_text(s0):
    if len(s0) == 0:
        return [],[]
    s = ""
    if isinstance(s0, list):
        for w in s0:
            s += " " + w
        s = s.lower()
    else:
        s = s0.lower()

    stop = set(stopwords.words('english'))
    tokens = nltk.word_tokenize(s)
    valid_tokens = [w for w in tokens if w not in stop]
    stemmer = nltk.stem.snowball.EnglishStemmer(ignore_stopwords=False)
    stemmed_tokens = [stemmer.stem(w) for w in valid_tokens]
    set_tokens = list(set(stemmed_tokens))
    punc = string.punctuation
    terms = []
    delete_words = ["'s"]
    for w in set_tokens:
        flag = True
        for c in w:
            if c not in punc:
                flag = False
            if w in delete_words or w in stop:
                flag = True
        if not flag:
            w1 = w.encode("utf-8")
            terms.append(w1)
    stop_words = list(set(tokens) - set(valid_tokens))
    return terms,stop_words
