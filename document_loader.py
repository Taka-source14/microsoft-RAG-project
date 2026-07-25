from pathlib import Path


def load_documents(folder_path: str = "documents") -> list[dict]:
    """
    Loads all .txt documents from the given folder.

    Each document is returned as a dictionary with:
    - source: file name
    - content: file content
    """
    folder = Path(folder_path)

    # Check if folder exists and is a directory
    if not folder.exists():
        raise FileNotFoundError(f"Klasör bulunamadı: {folder_path}")
    if not folder.is_dir():
        raise NotADirectoryError(f"Belirtilen yol bir klasör değil: {folder_path}")

    documents = []

    for file_path in folder.glob("*.txt"):
        try:
            content = file_path.read_text(encoding="utf-8").strip()
            
            # Load even if empty, or skip if size/content is empty. 
            # We will load it but keep it safe.
            documents.append({
                "source": file_path.name,
                "content": content
            })
        except Exception as e:
            # Handle potential file reading errors (permissions, encoding issues, etc.)
            print(f"Hata: {file_path.name} dosyası okunurken hata oluştu: {e}")

    return documents