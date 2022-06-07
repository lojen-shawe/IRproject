from collections import Counter
import numpy as np


def DF(tokens_set):
    DF = {}

    for i in range(len(tokens_set)):
        tokens = tokens_set[str(i + 1)]
        for w in tokens:
            try:
                DF[w].add(i)
            except:
                DF[w] = {i}
    for i in DF:
        DF[i] = len(DF[i])
    return DF


def doc_freq(word, DF):
    c = 0
    try:
        c = DF[word]
    except:
        pass
    return c


def TF_IDF(tokens_set, DF):
    doc = 0
    N = len(tokens_set)
    tf_idf = {}
    tokens = tokens_set[str(1)]

    for i in range(len(tokens_set)):
        if (i > 1):
            tokens = tokens_set[str(i)]

        counter = Counter(tokens)
        words_count = len(tokens)

        for token in np.unique(tokens):
            tf = counter[token] / words_count
            df = doc_freq(token, DF)
            idf = np.log((N + 1) / (df + 1))
            tf_idf[doc, token] = tf * idf
        doc += 1
    return tf_idf
