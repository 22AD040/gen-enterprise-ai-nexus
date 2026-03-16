from sklearn.metrics.pairwise import cosine_similarity

def similarity_search(query_embedding, embeddings, texts, k=5):

    scores = cosine_similarity([query_embedding], embeddings)[0]

    ranked = sorted(
        zip(scores, texts),
        key=lambda x: x[0],
        reverse=True
    )

    return ranked[:k]