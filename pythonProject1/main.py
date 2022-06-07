from collections import Counter

import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from num2words import num2words
import dectionary as d
import math
from textblob import TextBlob
import textprossing as processing
import TF_IDF as tfidf
import cosinesimilarilty as cosinsimilarity
import dectionary as dect
import evaluation as ev
import readingquery as rquery
import cluster as c
#from Regex import Regex

def search(query):
    docset = {}
    title=[]
    docset,title = dect.readingfile('CISI/CISI.ALL')
   # queryRegex = Regex()
   # qu = queryRegex.compile_string(rquery.Query()[query].upper())
   # q_tokens = queryRegex.result
    qry_set = {}
    qry_set = rquery.queryread('CISI/CISI.QRY')

    processed_set = {}
    proc_token_id = ""
    proc_token_text = ""

    for i in docset:
        doc_token_id = i
        processed_set[doc_token_id] = processing.preprocess(docset[str(i)])

  #  regex = Regex()
  #  sentence_regex = []
  #  for sentence in docset:
      #  sentence_regex.append(regex.compile_string(sentence))
   # fileReader = sentence_regex
   # tokens = regex.result
   # print(tokens)
    tokens_set = {}
    doc_token_id = ""
    doct_token_text = ""
    N=len(tokens_set)
    for i in processed_set:
        doc_token_id = i
        tokens_set[doc_token_id] = word_tokenize(processed_set[str(i)])

    DF = {}
    DF = tfidf.DF(tokens_set)

    tf_idf = {}
    tf_idf = tfidf.TF_IDF(tokens_set,DF)

    total_vocab = [x for x in DF]
    total_vocab_size=len(total_vocab)
    N = len(tokens_set)
    D = np.zeros((N, total_vocab_size))
    for i in tf_idf:
        try:
            ind = total_vocab.index(i[1])
            D[i[0]][ind] = tf_idf[i]
        except:
            pass
    ev.evaluation(docset, qry_set, D, N, total_vocab, DF)
   # average_precision,average_recall,F_Measure,Accuracy = ev.evaluation(docset,qry_set,,D,N,total_vocab,DF)
    Q = cosinsimilarity.cosine_similarity(10, query,D,N,total_vocab,DF)
    return Q

def searchcacm(query):
    docset = {}
    docset = dect.readingfile('cacm/cacm.all')
    qry_set = {}
    qry_set = rquery.queryread('cacm/query.text')

    processed_set = {}
    proc_token_id = ""
    proc_token_text = ""

    for i in docset:
        doc_token_id = i
        processed_set[doc_token_id] = processing.preprocess(docset[str(i)])

    tokens_set = {}
    doc_token_id = ""
    doct_token_text = ""
    N=len(tokens_set)
    for i in processed_set:
        doc_token_id = i
        tokens_set[doc_token_id] = word_tokenize(processed_set[str(i)])

    DF = {}
    DF = tfidf.DF(tokens_set)

    tf_idf = {}
    tf_idf = tfidf.TF_IDF(tokens_set,DF)

    total_vocab = [x for x in DF]
    total_vocab_size=len(total_vocab)
    N = len(tokens_set)
    D = np.zeros((N, total_vocab_size))
    for i in tf_idf:
        try:
            ind = total_vocab.index(i[1])
            D[i[0]][ind] = tf_idf[i]
        except:
            pass
    ev.evaluation(docset, qry_set, D, N, total_vocab, DF)
   # average_precision,average_recall,F_Measure,Accuracy = ev.evaluation(docset,qry_set,,D,N,total_vocab,DF)
    Q = cosinsimilarity.cosine_similarity(10, query,D,N,total_vocab,DF)
    return Q


if(__name__=='__main__'):
    Q = searchcacm("a")
    print(Q)

