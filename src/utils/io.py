import os

def load_documents(path: str):
    docs = []
    for fname in os.listdir(path):
        with open(os.path.join(path, fname), "r") as f:
            docs.append(f.read())
    return docs
