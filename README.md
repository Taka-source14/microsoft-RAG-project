# YBS Proje Takip Asistanı – Local RAG Project Management Assistant

## 1. Project Overview

This project is a terminal-based Local RAG MVP developed for the Microsoft Foundry Local / Local RAG AI Assistant project requirement.

The system allows users to ask natural language questions over local project documents. It reads local TXT, DOCX, and text-based PDF files, splits them into chunks, creates local vector representations, stores them in SQLite, retrieves the most relevant chunks with cosine similarity, and produces short source-grounded answers.

To support this, the implementation integrates:
- **Local RAG** & **Retrieval-Augmented Generation** concepts
- **Microsoft Foundry Local** ready interfaces
- Automated **document ingestion** (supporting TXT, DOCX, PDF parsing)
- Text **chunking**
- Text **embeddings** (with TF-IDF local fallback)
- Structured **vector search** and **SQLite vector store**
- **Semantic retrieval** based on **cosine similarity**
- **Prompt engineering** for safe context boundaries
- **Grounded answer generation** using extractive fallbacks
- Traceable **source citations** with chunk IDs and scores
- Complete **offline execution** with no cloud APIs

---

## 2. Assignment Alignment

The assignment document describes a Local RAG AI Assistant with Microsoft Foundry Local. The expected project is a local document Q&A assistant that retrieves relevant content from a small document collection and uses that retrieved context to generate answers.

This project implements the core RAG pipeline required by the document:
- Local document collection
- Document ingestion
- Chunking
- Local vector representation
- SQLite-based vector storage
- Semantic retrieval with cosine similarity
- Prompt construction
- Source-grounded answer generation
- Fallback behavior when the answer is not available in the documents
- CLI-based local interaction

---

## 3. Implemented RAG Pipeline

```text
Documents → Document Loader → Text Chunker → Embedding / Vector Representation → SQLite Vector Store → Semantic Retriever → Prompt Builder → Answer Generator → Source-Cited Answer
```

- **Document Loader:** Reads TXT, DOCX, and text-based PDF files from the documents folder.
- **Text Chunker:** Splits long documents into smaller passages.
- **Embedding / Vector Representation:** Converts chunks and user questions into local vector representations.
- **SQLite Vector Store:** Stores chunks and their vectors in `rag.db`.
- **Semantic Retriever:** Uses cosine similarity to retrieve the most relevant chunks.
- **Prompt Builder:** Prepares retrieved context for grounded answer generation.
- **Answer Generator:** Produces concise answers and displays source file names and chunk IDs.

---

## 4. Microsoft Foundry Local Context

The assignment document targets Microsoft Foundry Local for offline model inference. This project is structured with a Microsoft Foundry Local-ready architecture by separating embedding generation, vector storage, retrieval, prompt building, and answer generation into independent modules.

Current runtime mode:
- **Embedding mode:** TF-IDF fallback
- **Vector store:** SQLite `rag.db`
- **Retrieval:** cosine similarity
- **Answering:** source-grounded local fallback generation
- **Execution:** fully offline CLI application

When Microsoft Foundry Local is available in the environment, the embedding and answer generation layers can be extended to use Foundry Local embedding and chat models. In the current setup, the system uses TF-IDF fallback to keep the RAG pipeline working offline without cloud APIs or paid API keys.

---

## 5. Features

- Terminal-based Local RAG MVP
- Local document question answering
- TXT, DOCX, and text-based PDF support
- Automatic document chunking
- Local vector representation
- SQLite vector store
- Semantic retrieval with cosine similarity
- Prompt building
- Source-grounded answer generation
- Source file and chunk ID references
- Fallback response for unrelated questions
- Offline execution
- No cloud API required
- No paid API key required
- Microsoft Foundry Local-ready architecture

---

## 6. Supported File Types

- `.txt` (Plain text files)
- `.docx` (Microsoft Word documents)
- `.pdf` (text-based only)

Scanned PDFs are not supported because OCR is not implemented.

---

## 7. Installation

To install dependencies, run the following commands:
```powershell
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
```

---

## 8. Run the Application

To run the terminal CLI loop:
```powershell
python app.py
```

---

## 9. Expected Startup Output

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

## 10. Example Questions

- `RAG nedir?`
- `Bu projenin amacı nedir?`
- `Foundry Local nedir?`
- `Embedding ne işe yarar?`
- `Vector search ne işe yarar?`
- `Bu sistem hangi dosya türlerini destekliyor?`
- `Bugün hava nasıl?`
- `Bitcoin fiyatı kaç?`

Document-related questions should return concise source-based answers.
Unrelated or current-world questions should return:
`“Bu soruyla ilgili yerel dokümanlarda yeterli bilgi bulunamadı.”`

---

## 11. Repository Structure

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

## 12. How This Matches the Required Project

| Assignment Requirement | Project Implementation |
|---|---|
| Local document Q&A assistant | Implemented with CLI app |
| RAG pipeline | Implemented as local retrieval + grounded answer pipeline |
| Document ingestion | Implemented for TXT, DOCX, and text-based PDF |
| Chunking | Implemented with `text_chunker.py` |
| Embeddings / vector representation | Implemented with local TF-IDF fallback |
| SQLite storage | Implemented with `rag.db` |
| Semantic retrieval | Implemented with cosine similarity |
| Prompt engineering | Implemented with `prompt_builder.py` |
| Source citations | Implemented with source file and chunk ID |
| Offline execution | Implemented |
| Foundry Local architecture | Project is structured to be Foundry Local-ready |

---

## 13. Limitations

- Current runtime uses TF-IDF fallback instead of active Foundry Local models.
- Current answer generation is local extractive/source-grounded fallback.
- Full Foundry Local embedding and chat model activation depends on environment setup.
- Scanned PDFs are not supported.
- Very large document collections may require optimization.
- This is an MVP, not a production deployment.

---

## 14. Future Improvements

- Activate Microsoft Foundry Local embedding model
- Add Microsoft Foundry Local chat model generation
- Improve semantic ranking
- Add advanced vector database support
- Add OCR for scanned PDFs
- Add optional UI after CLI MVP
- Add automated evaluation metrics for answer quality

---

## 15. Final Statement

This project demonstrates a working Local RAG MVP pipeline for project management documents with offline execution, local document ingestion, chunking, vector-based retrieval, SQLite storage, prompt construction, and source-grounded answer generation. It is aligned with the Local RAG AI Assistant with Microsoft Foundry Local project requirements and is structured for future Foundry Local model integration.
