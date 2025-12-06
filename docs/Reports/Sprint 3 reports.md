# Sprint 3 Report (Dates from 11/6 to 12/2)

## YouTube link of Sprint 3 Video
[Watch on YouTube](https://youtu.be/6_CssNaEQqY)

---

# What's New

* Added a working **demo version of the SBYEC AI Chatbot** directly on the SBYEC website through a temporary integration.  
  Users can now open a chat window, ask natural-language questions, and receive answers based on real content from sbyec.org.

* The chatbot answers questions using automatically refreshed website data, including event information, lesson descriptions, programs, services, and contact details.

* Example queries that now work in the demo:  
  * “What events are coming up?”  
  * “When is Peppermints & Ponies?”  
  * “What programs does SBYEC offer?”  
  * “How can I contact SBYEC?”  
  * “What does Rising Stars include?”

* The chatbot operates in **demo mode**, meaning it is only available when our backend system is manually running.  
  When the backend is offline, users see a “Network error” message, which prevents misleading or partial responses.

* The chatbot is intentionally restricted to **SBYEC’s official content**.  
  If users ask questions unrelated to the website, the chatbot replies with a controlled fallback message to avoid misinformation.

* Delivered a full **Events Manual** for SBYEC staff, containing step-by-step tutorials (with screenshots) on how to add, edit, and manage events via The Events Calendar plugin.  
  This document enables staff members with no technical background to maintain their own event listings.

---

# Work Summary (Developer Facing)

Sprint 3 focused entirely on implementing the **end-to-end AI Chatbot System**, including crawling, content processing, vector storage, semantic retrieval, and integration with the live SBYEC website for demonstration.

The major development work consisted of:

### 1. Full Website Crawler
We implemented a dedicated crawler responsible for extracting structured data from **15 key SBYEC pages**, covering:
- Homepage  
- Events  
- Lesson subpages  
- Programs  
- Equine services  
- Mission and staff pages  
- Contact information  

Special logic was added to preserve **footer content** (address, phone, email) before removing navigation menus, scripts, or other unnecessary elements.

All cleaned content is merged into a single **22 KB master text file**, which serves as the canonical knowledge source for the chatbot.

### 2. Data Processing: Chunking and Embeddings
To support semantic search, we used:
- **500-character chunks**  
- **150-character overlap**  
- **RecursiveCharacterTextSplitter** for robust segmentation  
- **all-MiniLM-L6-v2 embedding model**, producing 384-dimensional vectors  

These embeddings are stored locally in **ChromaDB**, allowing highly efficient similarity search against user queries.

### 3. Retrieval-Augmented Generation (RAG) Pipeline
We implemented a custom RAG pipeline using LangChain:
- Query embedding  
- Top-k retrieval (k = 10 by default)  
- Context injection into a strict template  
- Running Llama 3.2 (1B or 3B) for answer generation  

Our prompt ensures:
- Answers must come only from retrieved website content  
- Specific rules for event recognition  
- Inclusion of address/phone/email when available  
- Automatic fallback to official contact info when uncertain  

This prevents hallucination and ensures accurate client-facing responses.

### 4. LLM Backend with Ollama
We integrated **Ollama** to run lightweight Llama 3.2 models:
- **1B model** for free-tier deployment compatibility  
- **3B model** for high-accuracy local testing  

Cold-start and warm-start performance metrics were evaluated to ensure the chatbot remains responsive under limited compute resources.

### 5. Flask REST API + ngrok Tunnel
Built a complete REST API with:
- `POST /api/chat`  
- `POST /api/refresh`  
- `GET /api/status`

Since free-tier hosting could not support the full chatbot stack this sprint, we exposed the API using **ngrok**, providing a temporary public HTTPS endpoint for demo use.

### 6. WordPress Website Integration
We embedded the chatbot on the SBYEC website using a **custom HTML + JavaScript block**, allowing users to:
- Open a floating chat window  
- Type questions  
- Receive live responses routed through our backend  

All interactions use secure HTTPS through the ngrok proxy.

### 7. System Stability and Testing
We conducted extensive tests on:
- Contact info accuracy  
- Program descriptions  
- Event extraction  
- Crawler reliability  
- Refresh consistency  
- RAG output quality  
- User UI responsiveness  

By the end of Sprint 3, the system demonstrated consistently correct answers for contact information, stable retrieval for lesson/program content, and improved accuracy on events after tuning.

---

# Technical Details: System Architecture

```text
sbyec.org (15 pages)
        │
        ▼
Web Crawler (BeautifulSoup)
        │
        ▼
data/sbyec_website_content.txt
        │
        ├── Chunking (500 chars, 150 overlap)
        └── Embeddings (MiniLM-L6-v2)
        ▼
ChromaDB (Vector Database)
        │
        └── Top-k similarity retrieval (k = 10)
        ▼
RAG Chatbot Engine (Ollama Llama 3.2)
        │
        └── Final Answer Generation
        ▼
Flask REST API
        │
        └── WordPress Chat Widget Integration
```

---

# Unfinished Work

The primary unfinished task of this sprint is **deploying the chatbot to a continuous, always-online hosting environment**, allowing it to operate without manual backend activation.

### Blockers identified:
- Free-tier cloud platforms cannot run Llama 3.2 due to RAM and time-limit constraints  
- WordPress requires HTTPS and restricted CORS to safely embed third-party APIs  
- Long-running inference services are disallowed or auto-suspended on free tiers  
- A permanent deployment environment requires additional configuration effort not achievable in a single sprint timeframe  

### Deferred to Sprint 4:
- Full deployment to a cloud or dedicated hosting environment  
- HTTPS hardening and domain-level CORS restrictions  
- Persistent "Ask a Question" chat widget  
- Monitoring, logging, and basic usage analytics  
- More aggressive accuracy tuning (especially for event extraction)


---


# Code Files for Review

Please review the following files, which contain all major Sprint 3 development:

* [website_crawler.py](https://github.com/ZY115/SBYEC/blob/main/code/backend/src/website_crawler.py)  
* [rag_chatbot_web_ready.py](https://github.com/ZY115/SBYEC/blob/main/code/backend/src/rag_chatbot_web_ready.py)  
* [auto_updater.py](https://github.com/ZY115/SBYEC/blob/main/code/backend/src/auto_updater.py)  
* [flask_api.py](https://github.com/ZY115/SBYEC/blob/main/code/backend/src/flask_api.py)  


---

# Retrospective Summary

## What Went Well
* Successfully built and integrated a working AI chatbot into the SBYEC website.
* Achieved stable, grounded answers using real SBYEC website content.
* Completed a thorough Events Manual that met all client expectations.
* RAG pipeline architecture is robust, documented, and ready for final deployment.

## What Could Be Improved
* The chatbot is not yet hosted in a cloud environment; uptime depends on manual backend activation.
* Query logging, analytics, and error monitoring need to be implemented after deployment.
* Some pages require more structured HTML cleanup to improve retrieval accuracy.

## Plans for Next Sprint
* Deploy the chatbot on a suitable hosting platform (Railway, Render, VPS).  
* Add a polished floating chat widget for full-time embedding on the SBYEC website.  
* Add monitoring, logs, and stability improvements.  
* Optimize retrieval strategies and chunking for higher accuracy.  
* Expand documentation for client workflows beyond events (program changes, staff profiles, etc.).
