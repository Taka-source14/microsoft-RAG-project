from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Global flag to track embedding mode
USE_FOUNDRY = False


def build_embeddings(chunks: list[dict]) -> tuple[list[dict], object]:
    """
    Takes document chunks and returns chunks with embeddings plus the fitted embedding model/vectorizer.
    """
    global USE_FOUNDRY
    try:
        # Attempt to import a hypothetical Foundry Local package
        import foundry_local_sdk
        # If found, configure it
        # model = foundry_local_sdk.load_embedding_model()
        # USE_FOUNDRY = True
        # ...
        raise ImportError()
    except ImportError:
        USE_FOUNDRY = False
        print("Foundry Local embedding model not available. Using local TF-IDF fallback for semantic retrieval.")

        texts = [chunk["content"] for chunk in chunks]
        vectorizer = TfidfVectorizer()
        if texts:
            tfidf_matrix = vectorizer.fit_transform(texts)
            embeddings = tfidf_matrix.toarray()
            for idx, chunk in enumerate(chunks):
                chunk["embedding"] = embeddings[idx].tolist()
        else:
            vectorizer.fit([""])

        return chunks, vectorizer


def embed_query(question: str, embedding_model: object) -> list[float]:
    """
    Converts user question into an embedding/vector using the same model/vectorizer.
    """
    if USE_FOUNDRY:
        # Placeholder for Foundry Local embedding query
        return []
    else:
        query_vector = embedding_model.transform([question]).toarray()[0]
        return query_vector.tolist()
