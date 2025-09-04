
---

# Technical Documentation – Knowledge Assistant (Support Ticket RAG System)

## 1. Overview

This notebook implements a **Knowledge Assistant** that helps a support team handle customer tickets efficiently. It uses a **Retrieval-Augmented Generation (RAG)** pipeline with a **Large Language Model (LLM)**. The output is structured in **MCP-compliant JSON** format, containing an answer, references, and an action requirement.

The project was deployed entirely on Google Colab using the T4 GPU setting.

---

## 2. Technologies Used

### Core Libraries

* **Python 3.11 (Notebook Kernel)** → Core programming environment.
* **Langchain / Transformers / OpenAI API (depending on the model used)** → For interacting with the LLM and structuring prompts.
* **FAISS / SentenceTransformers** → For embedding documents and performing vector similarity search.
* **json** → To parse and validate LLM outputs.
* **IPython / Jupyter** → Interactive environment for development, experimentation, and documentation.

### Data

* **Support Documentation** (Markdown/PDF/Policy text added into the notebook).
  Example categories:

  * Domain suspension policies
  * WHOIS accuracy requirements
  * Billing and payment procedures
  * Abuse handling and escalation guidelines

---

## 3. Workflow in the Notebook

### Step 1: Load Documents

* The notebook loads synthetic or real support policies (Markdown, text, or PDF).
* If PDFs are used, libraries like `PyPDF2` or `pdfplumber` extract text.

### Step 2: Chunking

* Long documents are split into smaller **chunks** (e.g., 400–500 tokens) with overlap to preserve context.

### Step 3: Embedding & Indexing

* Chunks are converted into numerical vectors using **SentenceTransformers embeddings**.
* Stored in a **FAISS vector index** for fast similarity search.

### Step 4: Retrieval

* A user support ticket (query) is embedded and compared against document vectors.
* The **top-k most relevant chunks** are retrieved as context.

### Step 5: MCP Prompting

* A structured **MCP prompt template** is built with:

  * **Role** → “You are a Knowledge Assistant for a support team.”
  * **Context** → Retrieved document chunks.
  * **Task** → Generate an answer + references + action\_required.
  * **Schema** → Strict JSON structure with 3 keys.

### Step 6: LLM Generation

* The query + context are passed into the LLM.
* The model outputs a JSON response.
* Example:

  ```json
  {
    "answer": "Your domain may have been suspended due to WHOIS inaccuracies. Please update your details and contact support.",
    "references": ["Policy: Domain Suspension Guidelines, Section 4.2"],
    "action_required": "escalate_to_abuse_team"
  }
  ```

### Step 7: Validation

* The JSON output is validated to ensure it has:

  * `"answer"` (string)
  * `"references"` (list of strings)
  * `"action_required"` (enum value)

### Step 8: Saving Results

* The structured JSON is written to the same directory as the documents.
* Each run can save a timestamped `.json` file for traceability.

---

## 4. Permissions/Login Credentials Needed

To run this notebook successfully with different Large Language Models (LLMs), a few authentication steps and permissions are required:

### Hugging Face Account

* You must have a **Hugging Face account** ([https://huggingface.co](https://huggingface.co)).
* This is needed to download and use models such as **Meta’s LLaMA 2** and **Mistral**.
* Once registered, you can generate a personal **Access Token** under your account settings (`Settings > Access Tokens`).
* This token must be set in your environment:

  ```bash
  export HUGGINGFACEHUB_API_TOKEN="your_token_here"
  ```

  or directly in the notebook:

  ```python
  import os
  os.environ["HUGGINGFACEHUB_API_TOKEN"] = "your_token_here"
  ```

### Meta LLaMA 2 Permissions

* To use **meta-llama/Llama-2-7b-chat-hf** (or other LLaMA 2 variants), you must **request access** from Meta via Hugging Face model card page.
* Approval is typically **granted within 60 minutes**, though in some cases it may take longer.
* Without this approval, attempts to load the model will result in a *“you don’t have permission”* error.

### Alternative Model – Mistral

* If LLaMA 2 access has not yet been approved, you can use **Mistral 7B Instruct** (`mistralai/Mistral-7B-Instruct-v0.2`) as a direct alternative.
* Mistral is open-access and requires only a Hugging Face account/token (no extra permission from Meta).
* The notebook is already compatible — you can switch models with a simple parameter change.

---
## 5. Example End-to-End Flow

1. Input Ticket:

   ```
   "My domain was suspended and I didn’t get any notice. How can I reactivate it?"
   ```

2. Retrieval finds:

   * **Domain Suspension Guidelines, Section 1.2 (Notification)**
   * **Reactivation Steps, Section 1.3**

3. LLM Output:

   ```json
   {
     "answer": "Domains may be suspended for missing WHOIS or abuse reports. To reactivate, update your WHOIS details or resolve billing issues. If related to abuse, the Abuse Team must review.",
     "references": [
       "Policy: Domain Suspension Guidelines, Section 1.2",
       "Policy: Domain Suspension Guidelines, Section 1.3"
     ],
     "action_required": "escalate_to_abuse_team"
   }
   ```

4. JSON saved to the same folder as the PDF docs.

---

## 6. Testing & Validation

### Simple Checks Implemented

* **Pipeline test** → Ensure that `resolve_ticket(query)` returns JSON with the 3 required keys.
* **Save test** → Ensure the function that saves JSON creates a valid file in the same directory.


---

## 7. Key Design Choices

* **RAG instead of plain LLM** → Ensures responses are grounded in company policies.
* **MCP JSON schema** → Provides consistent, structured output for integration.
* **Document chunking** → Improves retrieval accuracy by narrowing context windows.
* **File saving** → Keeps a local JSON log of responses aligned with the documents.

---

## 8. Future Extensions

* Improve retrieval with re-ranking (e.g., BM25 + FAISS hybrid).
* Add more domain-specific escalation categories.
* Evaluate with real support tickets to measure accuracy.

---

