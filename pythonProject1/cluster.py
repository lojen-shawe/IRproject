from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import dectionary as dect
import textprossing as processing

def cluster(processed_set,title):
    stop_words = stopwords.words('english')
    # tfidf vectorizer of scikit learn
    vectorizer = TfidfVectorizer(stop_words=stop_words, max_features=10000, max_df=0.5, use_idf=True, ngram_range=(1, 3))
    X = vectorizer.fit_transform(processed_set)
    print(X.shape)
    terms = vectorizer.get_feature_names()
    from sklearn.cluster import KMeans
    num_clusters = 10
    km = KMeans(n_clusters=num_clusters)
    km.fit(X)
    clusters = km.labels_.tolist()
    from sklearn.utils.extmath import randomized_svd
    U, Sigma, VT = randomized_svd(X, n_components=10, n_iter=100, random_state=122)
    lines = ""
    c=[]
    for i, comp in enumerate(VT):
        terms_comp = zip(title, comp)
        sorted_terms = sorted(terms_comp, key=lambda x: x[1], reverse=True)[:7]
        lines +=str(i)
        print("Concept " + str(i) + ": ")
        for t in sorted_terms:
            lines+=t[0]
            print(t[0])
        print(" ")
        c.append(lines)

    return c

if(__name__=='__main__'):
    docset, title = dect.readingfile('CISI/CISI.ALL')
    qry_set = {}
    #    qry_set = rquery.queryread()
    processed_set = {}
    proc_token_id = ""
    proc_token_text = ""
    for i in docset:
        doc_token_id = i
        processed_set[doc_token_id] = processing.preprocess(docset[str(i)])
    c = cluster(processed_set, title)
    print("looooloooooooo")
   # print(list(result))
    print(len(c))