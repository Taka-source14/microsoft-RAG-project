import sqlite3
import json
import os


def initialize_database(db_path: str = "rag.db") -> None:
    """
    Initializes the SQLite database and creates the chunks table if it does not exist.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chunks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            chunk_id INTEGER,
            content TEXT,
            embedding TEXT
        )
    """)
    conn.commit()
    conn.close()


def save_chunks(chunks: list[dict], db_path: str = "rag.db") -> None:
    """
    Saves a list of chunks with their embeddings to the SQLite database.
    """
    initialize_database(db_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    for chunk in chunks:
        embedding_str = json.dumps(chunk.get("embedding", []))
        cursor.execute("""
            INSERT INTO chunks (source, chunk_id, content, embedding)
            VALUES (?, ?, ?, ?)
        """, (chunk["source"], chunk["chunk_id"], chunk["content"], embedding_str))
    conn.commit()
    conn.close()


def load_chunks(db_path: str = "rag.db") -> list[dict]:
    """
    Loads all chunks with their deserialized embeddings from the SQLite database.
    """
    if not os.path.exists(db_path):
        return []

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT source, chunk_id, content, embedding FROM chunks")
    rows = cursor.fetchall()
    conn.close()

    chunks = []
    for row in rows:
        chunks.append({
            "source": row[0],
            "chunk_id": row[1],
            "content": row[2],
            "embedding": json.loads(row[3])
        })
    return chunks


def rebuild_vector_store(chunks: list[dict], embedding_model: object, db_path: str = "rag.db") -> None:
    """
    Drops the chunks table, re-initializes it, and saves the new chunks.
    """
    # Ensure chunks have embeddings
    for chunk in chunks:
        if "embedding" not in chunk:
            vector = embedding_model.transform([chunk["content"]]).toarray()[0].tolist()
            chunk["embedding"] = vector

    # Reset table
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS chunks")
    conn.commit()
    conn.close()

    # Re-initialize and save chunks
    save_chunks(chunks, db_path)
