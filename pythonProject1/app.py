from flask import Flask, jsonify

import dectionary as doc

import main as Main
import spellchecking as checking
import cluster as cluster

docsetcisi,title = doc.readingfile('CISI/CISI.ALL')
docsetcacm = doc.readingfile('cacm/cacm.all')

app = Flask(__name__)

#@app.route('/api/add_message', methods=['POST', 'GET'])
@app.route('/add_cluster')
def add_cluster():
    c = cluster.cluster(docsetcisi, title)
    return jsonify(c)


@app.route('/Searchcisi/<QueryText>')
def CISI(QueryText):

    check=checking.correct_sentence_spelling(QueryText)
    Q = Main.search(QueryText)
    print(Q)
    lsit = []
    for i in range(len(Q)):
        lsit.append({'id': str(Q[i]),'text': docsetcisi[str(Q[i])]})
    print(lsit)
    if(check != QueryText):
        return jsonify(check=str(check),list=lsit)
    else:
        return jsonify(check="null" ,list=lsit)


@app.route('/Searchcacm/<QueryText>')
def cacm(QueryText):
    Q = Main.searchcacm(QueryText)
    print(Q)
    lsit = []
    for i in range(len(Q)):
        lsit.append({'text': docsetcacm[str(Q[i])],'id': str(Q[i]) })
    print(lsit)

    return jsonify(lsit)


if __name__ == '__main__':

    app.run(debug=False, port=4000)
