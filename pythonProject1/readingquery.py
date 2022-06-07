def queryread(file):
    with open(file) as f:
        lines = ""
        for l in f.readlines():
            lines += "\n" + l.strip() if l.startswith(".") else " " + l.strip()
        lines = lines.lstrip("\n").split("\n")

    qry_set = {}
    qry_id = ""
    for l in lines:
        if l.startswith(".I"):
            qry_id = l.split(" ")[1].strip()
        elif l.startswith(".W"):
            qry_set[qry_id] = l.strip()[3:]
            qry_id = ""
    return qry_set