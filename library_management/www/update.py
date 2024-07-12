def before_insert(doc, method):
    if doc.doctype == "Library Member":
        if doc.last_name == "C":
            doc.last_name = "R"

