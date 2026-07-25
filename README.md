# YBS Proje Takip Asistanı – Local RAG Project Management Assistant

This project is a terminal-based Local RAG Project Management Assistant developed for the “Local RAG AI Assistant with Microsoft Foundry Local” assignment.

The system implements a complete local Retrieval-Augmented Generation pipeline:
- local document ingestion
- TXT, DOCX, and text-based PDF loading
- document chunking
- local vector representation
- SQLite vector store
- semantic retrieval
- cosine similarity
- prompt construction
- source-grounded answer generation
- source citations
- fallback behavior for unanswerable questions
- offline execution

---

## Local AI / Offline RAG Runtime

The assistant runs entirely locally and does not require cloud APIs, paid API keys, or external services. It uses local document processing, local vector representation, local SQLite storage, local semantic retrieval, and local source-grounded answer generation.

Current runtime mode:
- Embedding mode: TF-IDF fallback
- Vector store: SQLite rag.db
- Retrieval: cosine similarity
- Answering: local source-grounded fallback generation
- Execution: fully offline CLI application

The project is designed with a Microsoft Foundry Local-ready architecture. The embedding and answer generation layers are modular, so they can be extended to use Microsoft Foundry Local embedding and chat models when Foundry Local is available in the environment.

---

## Assignment Alignment

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

## Implemented RAG Pipeline

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

## Features

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

## Supported File Types

- `.txt` (Plain text files)
- `.docx` (Microsoft Word documents)
- `.pdf` (text-based only)

Scanned PDFs are not supported because OCR is not implemented.

---

## Installation

To install dependencies, run the following commands:
```powershell
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
```

---

## Run the Application

To run the terminal CLI loop:
```powershell
python app.py
```

---

## Expected Startup Output

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

## Example Questions

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

## Repository Structure

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

## How This Matches the Required Project

| Assignment Requirement | Project Implementation |
|---|---|
| Local Q&A assistant | Implemented as terminal-based CLI assistant |
| RAG pattern | Implemented with retrieval + grounded answer generation |
| Local document collection | Implemented with documents/ folder |
| Document ingestion | Implemented in document_loader.py |
| Chunking | Implemented in text_chunker.py |
| Embeddings / vector representation | Implemented with local TF-IDF fallback |
| SQLite vector store | Implemented with rag.db |
| Semantic retrieval | Implemented with cosine similarity |
| Prompt engineering | Implemented in prompt_builder.py |
| Source citations | Implemented with source file and chunk ID |
| Offline execution | Implemented |
| Microsoft Foundry Local architecture | Project is structured to be Foundry Local-ready |

---

## Limitations

- Current runtime uses TF-IDF fallback instead of active Foundry Local models.
- Current answer generation is local extractive/source-grounded fallback.
- Full Foundry Local embedding and chat model activation depends on environment setup.
- Scanned PDFs are not supported.
- Very large document collections may require optimization.
- This is an MVP, not a production deployment.

---

## Future Improvements

- Activate Microsoft Foundry Local embedding model
- Add Microsoft Foundry Local chat model generation
- Improve semantic ranking
- Add advanced vector database support
- Add OCR for scanned PDFs
- Add optional UI after CLI MVP
- Add automated evaluation metrics for answer quality

---

## Final Statement

This project demonstrates a working Local RAG MVP pipeline for project management documents with offline execution, local document ingestion, chunking, vector-based retrieval, SQLite storage, prompt construction, source-grounded answer generation, and Microsoft Foundry Local-ready architecture.

---

## What I Learned

During this project, I learned how a Local RAG system works end-to-end. I practiced how to build a local document question-answering assistant by combining document ingestion, text chunking, local vector representation, semantic retrieval, prompt construction, and source-grounded answer generation.

Key learning outcomes:

- Understanding the Retrieval-Augmented Generation (RAG) pattern: retrieve, augment, and generate
- Loading and processing local TXT, DOCX, and text-based PDF documents
- Splitting long documents into smaller chunks for better retrieval
- Creating local vector representations for document chunks and user questions
- Storing document chunks and vectors in a local SQLite database
- Using cosine similarity for semantic retrieval
- Building prompts with retrieved context to reduce hallucination risk
- Returning source-cited answers instead of unsupported responses
- Designing the project with a Microsoft Foundry Local-ready architecture
- Keeping the system functional offline without cloud APIs or paid API keys