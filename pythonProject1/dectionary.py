def readingfile(file):
    with open(file) as CISI_file:
        lines = ""
        for l in CISI_file.readlines():
            lines += "\n" + l.strip() if l.startswith(".") else " " + l.strip()
        lines = lines.lstrip("\n").split("\n")

    docset = {}
    title = []
    doc_id = ""
    doc_text = ""
    for l in lines:
        if l.startswith(".I"):
            doc_id = l.split(" ")[1].strip()
        elif l.startswith(".X"):
            docset[doc_id] = doc_text.lstrip(" ")
            doc_id = ""
            doc_text = ""
        else:
            doc_text += l.strip()[3:] + " "

    for l in lines:
        if l.startswith(".T"):
            doc_text += l.strip()[3:] + " "
            title.append(doc_text)

    return docset,title
#if __name__=="__main__":
 #   doc={}
  #  title={}
   # doc,title= readingfile('CISI/CISI.ALL')
    #print(title)
   # return ""