import numpy as np
from collections import Counter
from nltk.tokenize import word_tokenize
import textprossing as tp
import TF_IDF as t
import math

def cosine_sim(a, b):
    cos_sim = np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))
    return cos_sim


def gen_vector(tokens,N,total_vocab,DF):
    Q = np.zeros((len(total_vocab)))

    counter = Counter(tokens)
    words_count = len(tokens)

    query_weights = {}

    for token in np.unique(tokens):

        tf = counter[token] / words_count
        df = t.doc_freq(token,DF)
        idf = math.log((N + 1) / (df + 1))

        try:
            ind = total_vocab.index(token)
            Q[ind] = tf * idf
        except:
            pass
    return Q


def cosine_similarity(k, query,D,N,total_vocab,DF):
    preprocessed_query = tp.preprocess(query)
    tokens = word_tokenize(str(preprocessed_query))

    d_cosines = []

    query_vector = gen_vector(tokens,N,total_vocab,DF)

    for d in D:
        d_cosines.append(cosine_sim(query_vector, d))

    out = np.array(d_cosines).argsort()[-k:][::-1]

    return out
