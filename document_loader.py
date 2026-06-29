from pathlib import Path


def load_documents(folder_path: str = "documents") -> list[dict]:
    """
    Loads all .txt documents from the given folder.

    Each document is returned as a dictionary with:
    - source: file name
    - content: file content
    """

    folder = Path(folder_path)

    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder_path}")

    documents = []

    for file_path in folder.glob("*.txt"):
        content = file_path.read_text(encoding="utf-8").strip()

        documents.append({
            "source": file_path.name,
            "content": content
        })

    return documents