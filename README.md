# Proje Takip Asistanı – Local RAG Project Management Assistant

## 2. Overview

“ Proje Takip Asistanı is a terminal-based Local RAG MVP that implements a complete local Retrieval-Augmented Generation workflow for project management documents. The system performs document ingestion, chunking, local vector representation, SQLite vector storage, semantic retrieval with cosine similarity, prompt construction, and source-grounded answer generation.”

“The project is designed with a Microsoft Foundry Local ready architecture. In the current local setup, the system runs fully offline using TF-IDF vectorization as the local embedding fallback. This allows the RAG pipeline to remain functional without cloud APIs, paid API keys, or external services.”

This is a working terminal-based Local RAG MVP that lets users ask questions over local project documents.

---

## 3. Problem Statement

Project documents are usually spread across different files such as plans, requirements, risks, notes, and reports. Manually searching them takes time. This assistant creates a local searchable knowledge base and answers questions with source references.

---

## 4. Implemented RAG Pipeline

```text
Documents → Document Loader → Text Chunker → Local Embeddings / Vector Representation → SQLite Vector Store → Semantic Retriever → Prompt Builder → Answer Generator → Source-Cited Answer
```

- **Document Loader** reads TXT, DOCX, and text-based PDF files from the documents folder during document ingestion.
- **Text Chunker** splits long documents into smaller chunks.
- **Embedding** layer creates local vector representations.
- **SQLite vector store** saves chunks and vectors in `rag.db`.
- **Semantic Retriever** calculates cosine similarity between the question and stored chunks.
- **Prompt Builder** prepares grounded context from retrieved chunks.
- **Answer Generator** returns concise answers with source citations.

---

## 5. Current Runtime Mode

Current runtime mode:
- **Embedding mode:** TF-IDF fallback
- **Vector store:** SQLite `rag.db`
- **Retrieval:** cosine similarity
- **Answering:** source-grounded local extractive generation
- **Execution:** fully offline terminal-based application

This still follows the RAG pipeline structure locally.

---

## 6. Microsoft Foundry Local Ready Architecture

This project was structured to be Microsoft Foundry Local ready. The current implementation already separates embedding generation, vector storage, retrieval, prompt building, and answer generation into independent modules. This makes it possible to replace the TF-IDF fallback with Foundry Local embedding and chat models in a future environment where Foundry Local is installed.

---

## 7. Features

- Terminal-based Local RAG MVP
- Local document question answering
- TXT, DOCX, and text-based PDF ingestion
- Automatic chunking
- Local vector representation
- SQLite vector storage
- Semantic retrieval with cosine similarity
- Prompt construction
- Source-grounded answer generation
- Source file and chunk ID references
- Fallback behavior for unrelated questions
- Fully offline execution
- No cloud API required
- No paid API key required

---

## 8. Supported File Types

- `.txt` (Plain text files)
- `.docx` (Microsoft Word documents)
- `.pdf` (text-based only)

Scanned PDFs are not supported because OCR is not implemented.

---

## 9. Installation

To install dependencies, run the following commands:
```powershell
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
```

---

## 10. Run

To run the interactive CLI loop:
```powershell
python app.py
```

---

## 11. Expected Startup Output

```text
==================================================
   YBS Proje Takip Asistanı (Local RAG Pipeline)
==================================================
Supported file types: .txt, .docx, .pdf
Uygulama başlatılıyor...

Documents loaded: 6
Chunks created: 119
Embedding mode: TF-IDF fallback
Vector store: rag.db
RAG pipeline ready.

Soru sorabilirsiniz. Çıkmak için 'q', 'quit', 'exit' veya 'çıkış' yazın.
```

---

## 12. Example Questions

- `RAG nedir?`
- `Bu projenin amacı nedir?`
- `Foundry Local nedir?`
- `Embedding ne işe yarar?`
- `Vector search ne işe yarar?`
- `Bu sistem hangi dosya türlerini destekliyor?`
- `Bugün hava nasıl?`
- `Bitcoin fiyatı kaç?`

Document-related questions return concise source-based answers.
Unrelated/current-world questions return:
`“Bu soruyla ilgili yerel dokümanlarda yeterli bilgi bulunamadı.”`

---

## 13. Repository Structure

```text
Local RAG Project Management Assistant/
├── app.py
├── document_loader.py
├── text_chunker.py
├── embedding_generator.py
├── vector_store.py
├── semantic_retriever.py
├── prompt_builder.py
├── response_generator.py
├── retriever.py
├── requirements.txt
├── README.md
├── .gitignore
├── documents/
├── sample_documents/
├── docs/
└── tests/
```

---

## 14. Limitations

- Current runtime uses TF-IDF fallback instead of active Foundry Local models.
- Fallback answer generation is extractive and source-grounded.
- Scanned PDFs are not supported.
- Very large document collections may require optimization.
- This is an MVP, not a production deployment.

---

## 15. Future Improvements

- Activate Microsoft Foundry Local embedding model
- Add Foundry Local chat model generation
- Improve semantic ranking
- Add advanced vector database support
- Add OCR for scanned PDFs
- Add optional UI after CLI MVP

---

## 16. Final Statement

“This project demonstrates a working Local RAG MVP pipeline for project management documents with offline execution, local document ingestion, vector-based retrieval, SQLite storage, prompt construction, and source-grounded answer generation.”
