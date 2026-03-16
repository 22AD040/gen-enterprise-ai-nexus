class VectorStore:

    def __init__(self):
        self.embeddings = None
        self.texts = None

    def add(self, embeddings, texts):

        self.embeddings = embeddings
        self.texts = texts

    def get(self):

        return self.embeddings, self.texts