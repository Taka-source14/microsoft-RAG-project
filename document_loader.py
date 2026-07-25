from pathlib import Path
from docx import Document
from pypdf import PdfReader


def load_txt_file(file_path: Path) -> str:
    """Reads a .txt file with UTF-8 encoding."""
    return file_path.read_text(encoding="utf-8").strip()


def load_docx_file(file_path: Path) -> str:
    """Reads a .docx file using python-docx."""
    doc = Document(file_path)
    paragraphs = [p.text for p in doc.paragraphs]
    return "\n".join(paragraphs).strip()


def load_pdf_file(file_path: Path) -> str:
    """Reads a text-based .pdf file using pypdf."""
    reader = PdfReader(file_path)
    text_parts = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            text_parts.append(text)
    return "\n".join(text_parts).strip()


def load_documents(folder_path: str = "documents") -> list[dict]:
    """
    Loads all .txt, .docx, and .pdf documents from the given folder.

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

    for file_path in folder.iterdir():
        if file_path.is_dir():
            continue

        suffix = file_path.suffix.lower()
        if suffix not in [".txt", ".docx", ".pdf"]:
            continue

        try:
            content = ""
            if suffix == ".txt":
                content = load_txt_file(file_path)
            elif suffix == ".docx":
                content = load_docx_file(file_path)
            elif suffix == ".pdf":
                content = load_pdf_file(file_path)

            # Skip the file if it has no readable text (empty or scanned PDF)
            if not content:
                print(f"Uyarı: {file_path.name} dosyasında okunabilir metin bulunamadı. Dosya atlandı.")
                continue

            documents.append({
                "source": file_path.name,
                "content": content
            })
        except Exception as e:
            # Handle potential file reading errors (permissions, encoding issues, etc.)
            print(f"Hata: {file_path.name} dosyası okunurken hata oluştu: {e}")

    return documents