# YBS Proje Takip Asistanı (Local RAG Project Management Assistant)

This project is a terminal-based Local RAG MVP. It implements document loading, chunking, local embedding/vector representation, SQLite vector storage, semantic retrieval with cosine similarity, prompt building, and source-based answer generation. If Microsoft Foundry Local is available, the architecture is ready for local model integration. If Foundry Local is not available, the system runs fully offline using a TF-IDF fallback retrieval mode.

---

## 1. Project Overview & Problem Solved

Managing project timelines, requirements, and deliverables can involve scanning through long document files. This project acts as an offline, private, and local **Retrieval-Augmented Generation (RAG)** assistant. It reads your project documents and answers natural language questions using only the context found within those files.

This solves the problem of information accessibility in project management without relying on cloud-based LLM APIs, preserving data privacy and ensuring complete offline functionality.

---

## 2. Current Implemented RAG Pipeline

The system utilizes the following local data flow:
```text
Documents Folder → Document Loader → Text Chunker → TF-IDF Fallback Embedding → SQLite Vector Store (rag.db) → Cosine Similarity Semantic Retriever → Prompt Builder → Extractive Fallback Generator → Source-Cited Answer
```

1. **Document Loader (`document_loader.py`):** Loads and reads `.txt` (UTF-8), Word `.docx`, and text-based `.pdf` files. Skips scanned (image-only) PDFs or empty files and raises a warning.
2. **Text Chunker (`text_chunker.py`):** Splits document contents into chunks of maximum 800 characters, respecting paragraph and sentence boundaries.
3. **Embedding Generator (`embedding_generator.py`):** Computes vector embeddings. When Microsoft Foundry Local SDK is absent, it uses a local `scikit-learn` TF-IDF vectorizer fallback.
4. **Vector Store (`vector_store.py`):** Rebuilds and stores all chunks, sources, and vector lists in a local SQLite database named `rag.db`.
5. **Semantic Retriever (`semantic_retriever.py`):** Transforms queries into vectors and scores all database chunks using **Cosine Similarity**. Matches below a `0.25` similarity score are ignored. If no matches are found, it falls back to the keyword-based retriever.
6. **Prompt Builder (`prompt_builder.py`):** Combines the user query with matching context blocks to build a grounded prompt in Turkish.
7. **Response Generator (`response_generator.py`):** Runs the answer generator. Since Foundry Local is in fallback mode, it triggers the local extractive engine to retrieve the most relevant sentence structures and lists sources with their similarity scores.

---

## 3. Supported File Types
* **`.txt`**: Read with standard UTF-8 encoding.
* **`.docx`**: Parsed using `python-docx`.
* **`.pdf`**: Text-based PDFs parsed using `pypdf`. (Scanned, image-based, or non-text PDFs are skipped with a warning).

---

## 4. Installation & Setup

Ensure Python 3.8+ is installed on your Windows system.

### Step 1: Create and Activate Virtual Environment
```powershell
python -m venv venv
venv\Scripts\activate
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 5. Running the Application

To run the terminal-based interactive CLI loop, execute:
```bash
python app.py
```

### Expected Startup Terminal Output:
```text
==================================================
   YBS Proje Takip Asistanı (Local RAG Pipeline)  
==================================================
Supported file types: .txt, .docx, .pdf
Uygulama başlatılıyor...

Documents loaded: 6
Chunks created: 580
Foundry Local embedding model not available. Using local TF-IDF fallback for semantic retrieval.
Embedding mode: TF-IDF fallback
Vector store: rag.db
RAG pipeline ready.

Soru sorabilirsiniz. Çıkmak için 'q', 'quit', 'exit' veya 'çıkış' yazın.

Soru: 
```

---

## 6. Example Questions

Once the application is running, you can test it with the following questions:

| Question | Expected Behavior |
| --- | --- |
| `RAG nedir?` | Returns a concise explanation and links source/chunk metadata |
| `Bu projenin amacı nedir?` | Returns the project goal from `proje_amaci.txt` |
| `Foundry Local nedir?` | Returns details from the document mentioning Foundry Local |
| `Embedding ne işe yarar?` | Returns embedding explanations |
| `Vector search ne işe yarar?` | Returns vector search explanations |
| `Bugün hava nasıl?` | Returns fallback message: *"Bu soruyla ilgili yerel dokümanlarda yeterli bilgi bulunamadı."* |
| `Bitcoin fiyatı kaç?` | Returns fallback message: *"Bu soruyla ilgili yerel dokümanlarda yeterli bilgi bulunamadı."* |

---

## 7. Current Limitations & Future Improvements

### Current Limitations:
* **Honest Foundry Local Status:** Currently running in **fallback mode** (using local TF-IDF embeddings and an extractive fallback response generation engine) since the Microsoft Foundry Local environment is not installed on this system.
* **No OCR Support:** Scanned or image-only PDF files cannot be processed and are skipped.
* **Simplified Fallback Generator:** The fallback response generator extracts sentences directly from matching chunks; it does not synthesize new text.

### Future Improvements:
* **Direct Microsoft Foundry Local Integration:** Hooking up dense embedding and chat models once the Foundry Local SDK becomes available.
* **SQLite-vss / FAISS Integration:** Replacing linear cosine similarity checks with structured vector index matching for large-scale operations.
* **OCR support:** Integrating `pytesseract` to extract text from scanned documents.
