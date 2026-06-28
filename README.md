# YBS Project Tracking Assistant

## Local RAG Project Management Assistant with Microsoft Foundry Local

YBS Project Tracking Assistant is a local Retrieval-Augmented Generation (RAG) application designed to support project management and progress tracking in Management Information Systems (MIS/YBS) projects.

The application answers user questions by retrieving relevant information from local project documents such as project goals, weekly plans, task lists, delivery criteria, risks, and presentation notes. Instead of generating answers only from the model’s general knowledge, the system first searches the local document collection and then generates a grounded response using the retrieved context.

This project was developed as part of the Microsoft Türkiye Summer School program under the topic:

**Building Your First Local RAG Application with Foundry Local**

---

## Project Purpose

The main purpose of this project is to build a simple, useful, and locally running AI assistant that helps users follow and manage a project more effectively.

The assistant can answer questions such as:

* What is the goal of the project?
* What tasks should be completed this week?
* What are the project delivery criteria?
* Which risks should be considered?
* How should the project be presented?
* What is RAG and how is it used in this project?
* What documents are used as the knowledge base?

This makes the project useful not only as a technical RAG implementation, but also as a practical project management support tool.

---

## What is RAG?

RAG stands for **Retrieval-Augmented Generation**.

It is an AI approach where the system:

1. Retrieves relevant information from a document collection.
2. Adds the retrieved information as context.
3. Generates an answer based on that context.

In this project, the assistant does not answer randomly or only from general model knowledge. It first searches the project documents and then produces an answer using the most relevant document chunks.

---

## Key Features

* Local document-based question answering
* Retrieval-Augmented Generation pipeline
* Microsoft Foundry Local integration
* Local inference without cloud dependency
* Project management focused knowledge base
* Source-aware answers
* Simple and understandable project structure
* Suitable for MIS/YBS project tracking scenarios

---

## Example Use Case

A user asks:

```text
What should I complete in the second week of the project?
```

The system searches the local project documents, finds the relevant part from the weekly plan, and generates an answer such as:

```text
In the second week, you should focus on preparing the project documents, splitting them into chunks, generating embeddings, and testing the retrieval process.
```

The assistant may also show the source document:

```text
Source: weekly_plan.txt
```

---

## Project Architecture

The basic workflow of the project is:

```text
Local Documents
      ↓
Document Loading
      ↓
Text Chunking
      ↓
Embedding Generation
      ↓
Similarity Search
      ↓
Relevant Context Retrieval
      ↓
Answer Generation with Foundry Local
      ↓
User Response
```

---

## Technologies Used

* Python
* Microsoft Foundry Local
* RAG architecture
* Embeddings
* Cosine similarity
* Local text documents
* Streamlit or CLI interface
* SQLite, optional for persistent storage

---

## Project Folder Structure

```text
ybs-rag-project-assistant/
│
├── app.py
├── rag_pipeline.py
├── document_loader.py
├── requirements.txt
├── README.md
│
├── documents/
│   ├── project_goal.txt
│   ├── weekly_plan.txt
│   ├── task_list.txt
│   ├── delivery_criteria.txt
│   ├── risks.txt
│   ├── presentation_notes.txt
│   └── rag_explanation.txt
│
└── tests/
    └── test_questions.md
```

---

## Documents Used in the Knowledge Base

The assistant uses a small local document collection related to the project management process.

Example documents:

| Document                 | Description                                   |
| ------------------------ | --------------------------------------------- |
| `project_goal.txt`       | Explains the purpose and scope of the project |
| `weekly_plan.txt`        | Contains weekly project activities            |
| `task_list.txt`          | Lists project tasks and responsibilities      |
| `delivery_criteria.txt`  | Defines the expected final deliverables       |
| `risks.txt`              | Describes possible project risks              |
| `presentation_notes.txt` | Includes notes for the final presentation     |
| `rag_explanation.txt`    | Explains RAG and its role in the project      |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/ybs-rag-project-assistant.git
cd ybs-rag-project-assistant
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the Application

For a simple command-line version:

```bash
python app.py
```

For a Streamlit interface:

```bash
streamlit run app.py
```

After running the application, the user can ask questions about the project documents.

Example:

```text
What are the delivery criteria of this project?
```

---

## How It Works

### 1. Document Loading

The system reads local text documents from the `documents/` folder.

### 2. Text Chunking

Long documents are split into smaller text chunks so that the system can search more accurately.

### 3. Embedding Generation

Each chunk is converted into a numerical vector representation using an embedding model.

### 4. Similarity Search

When the user asks a question, the question is also converted into an embedding. The system compares the question embedding with document chunk embeddings and retrieves the most relevant chunks.

### 5. Context-Aware Answer Generation

The retrieved chunks are added to the prompt as context. Then the local language model generates an answer based only on the provided context.

---

## Example Questions

The assistant can answer questions like:

```text
What is the main goal of this project?
```

```text
Which tasks should be completed in Week 1?
```

```text
What are the expected deliverables?
```

```text
What are the possible risks of the project?
```

```text
How does RAG work in this application?
```

```text
How should I explain this project in the final presentation?
```

---

## Expected Output Example

User question:

```text
What is the purpose of this project?
```

Assistant answer:

```text
The purpose of this project is to develop a local RAG-based project tracking assistant that helps users access project-related information from local documents. The system retrieves relevant information from project documents and generates grounded answers using Microsoft Foundry Local.

Source: project_goal.txt
```

---

## Project Deliverables

The final version of this project will include:

* A working local RAG assistant
* Local project management documents
* Document loading and chunking logic
* Embedding-based retrieval
* Answer generation with Microsoft Foundry Local
* Source-aware responses
* README documentation
* Test questions and results
* Demo video or presentation screenshots

---

## Test Plan

The project will be tested with two types of questions:

### Answerable Questions

These are questions where the answer exists in the local documents.

Example:

```text
What are the project delivery criteria?
```

### Unanswerable Questions

These are questions where the answer does not exist in the local documents.

Example:

```text
What is the weather today?
```

In such cases, the assistant should not hallucinate. It should respond with a message such as:

```text
I could not find enough information in the project documents to answer this question.
```

---

## Evaluation Criteria

The project will be evaluated based on:

* Correct retrieval of relevant document chunks
* Quality of generated answers
* Ability to avoid unsupported answers
* Clear source indication
* Simple and understandable user experience
* Clean code structure
* Complete documentation

---

## Why This Project is Useful

Project documents are often scattered across different files and notes. Users may spend time searching for information manually. This assistant helps users access project-related information faster by allowing them to ask natural language questions.

From a Management Information Systems perspective, this project demonstrates how AI can support:

* Knowledge management
* Project tracking
* Information retrieval
* Decision support
* Documentation management
* Productivity improvement

---

## Future Improvements

Possible future improvements include:

* Adding PDF and DOCX support
* Storing embeddings in SQLite
* Adding a Streamlit web interface
* Adding file upload support
* Improving source citation quality
* Adding task status tracking
* Adding multilingual support
* Creating a dashboard for project progress
* Exporting project summaries automatically

---

## Project Summary

YBS Project Tracking Assistant is a simple and practical local RAG application that helps users track project progress by answering questions from project documents. It combines document retrieval and local AI response generation to create a useful assistant for project management scenarios.

The project is designed to be beginner-friendly, locally runnable, and suitable for demonstrating the core logic of Retrieval-Augmented Generation using Microsoft Foundry Local.
