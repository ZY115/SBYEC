# Sprint 4 Report (Dates from 1/15 to 2/15)

## [YouTube link of Sprint 4 Video](https://youtu.be/b033JsfVcbE)
<p align="center">
  <img src="https://github.com/ZY115/SBYEC/blob/main/docs/Reports/Chatbot%20demo%201.png" width="45%"/>
  <img src="https://github.com/ZY115/SBYEC/blob/main/docs/Reports/Chatbot%20demo%202.png" width="45%"/>
</p>

## What's New
 * Deployed fully automated SBYEC chatbot to Hugging Face Spaces (24/7 public access)
 * Integrated Groq Llama 3.3 70B API for improved response quality
 * Implemented RAG-based knowledge retrieval using FAISS vector index
 * Enabled automated daily website crawling and index updates via GitHub Actions
 * Added tiered retrieval system to reduce unnecessary LLM API calls
 * Optimized cold-start performance by pre-loading vector index
 * The chatbot now supports approximately 14,400 LLM-powered queries per day under Groq’s free tier limits.
 *    Simple questions such as:
 *     - How to contact SBYEC 
 *     - Where is the location?
 * Which are answered without calling the LLM API, conserving quota through a tiered retrieval mechanism.

## Work Summary
### 1. Overall
   This sprint focused on transitioning the chatbot from a locally hosted prototype to a fully cloud-deployed production system. The team redesigned the architecture to eliminate dependency on Ollama and local runtime environments, migrating the backend to Hugging Face Spaces and integrating Groq’s Llama 3.3 70B API. A retrieval pipeline was implemented using sentence-transformers embeddings and FAISS indexing to enable efficient semantic search over crawled website content. We also developed a GitHub Actions workflow to automate the daily crawl → index → deploy cycle, ensuring continuous synchronization with the live website. Major barriers included API quota limitations, model deprecation issues with Gemini, and cold-start latency, which were addressed through provider migration, retrieval tiering, and pre-built vector indexing. Key learnings include managing free-tier infrastructure constraints, optimizing API usage, and designing sustainable automation pipelines.


### 2. Structure
We restructured the retrieval system to persist vector embeddings instead of rebuilding them at startup.
```
sbyec.org (15 pages)
        │
        ▼
Web Crawler 
        │
        ▼
data/sbyec_website_content.txt
        │
        ├── Chunking 
        └── Sentence-Transformer Embeddings
        ▼
FAISS Vector Index (Persisted)
        │
        ▼
Semantic Retrieval
        │
        ▼
Groq Llama 3.3 70B
        │
        ▼
Final Response
```

The FAISS index now loads in approximately one second during startup, dramatically reducing cold-start time.

### 3. Fully Automated Update Pipeline

We implemented a GitHub Actions workflow that runs on a scheduled basis.

The automated pipeline:

- Crawls 15 key SBYEC pages

- Regenerates cleaned text content

- Rebuilds the FAISS vector index

- Commits updates to GitHub

- Pushes changes to Hugging Face

- Triggers automatic redeployment

This ensures the chatbot always reflects the latest website content without manual backend intervention.

### 4. Tiered Retrieval Optimization

To conserve API usage, we implemented a two-tier answering system:

Tier 1 — Direct Extraction
Contact-related questions are answered using pattern matching on retrieved text.
No LLM API call is made.

Tier 2 — LLM Generation
Only synthesis or reasoning-based questions are sent to Groq’s LLM.

This significantly extends free-tier sustainability and improves cost efficiency.

System Stability and Validation

We conducted testing on:

- Contact information accuracy

- Program descriptions

- Lesson types (Private, Group, Rising Stars)

- Event queries (Spring Farm Friends, Peppermints & Ponies, etc.)

- Location queries

- Team member information

- Cold start performance

- Automated refresh reliability

The system consistently returned grounded responses based on official website content.

## Unfinished Work
At this time, there are no unfinished issues or user stories carried over from this sprint. All planned tasks were completed and properly closed in GitHub with their acceptance criteria verified.
In the next sprint, we plan to meet with the client to gather feedback and determine whether any additional features or refinements are desired. We will also consult with the instructor to identify potential improvements to the AI chatbot system, particularly in terms of usability, deployment stability, and long-term maintainability.

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:

 * [URL of issue 1](https://github.com/users/ZY115/projects/2/views/1?pane=issue&itemId=132215926&issue=ZY115%7CSBYEC%7C12)

 
 ## Incomplete Issues/User Stories
NONE
 

## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality:
 * [build_index.py](https://github.com/ZY115/SBYEC/blob/main/code/backend/src/build_index.py)
 * [update-content.yml](https://github.com/ZY115/SBYEC/blob/main/.github/workflows/update-content.yml)
 * [app.py](https://github.com/ZY115/SBYEC/blob/main/app.py)
 * [requirements.txt](https://github.com/ZY115/SBYEC/blob/main/requirements.txt)
 * [data/sbyec_website_content.txt](https://github.com/ZY115/SBYEC/blob/main/data/sbyec_website_content.txt)
## Retrospective Summary
Here's what went well:
  * Our team successfully refactored the chatbot architecture into modular components, such as crawler, knowledge base,and API service, which improved clarity and maintainability.
  * We improved collaboration by clearly dividing responsibilities, likebackend deployment, RAG pipeline ,and crawler automation, which helped us move efficiently without blocking each other.
  * We became more comfortable working with deployment environments and external APIs, which strengthened our understanding of real world system constraints beyond local development.
 
Here's what we'd like to improve:
   * We plan to improve documentation clarity, particularly around deployment instructions, to make it easier for future developers or the client to understand the system setup.
   * We would like to establish a more structured testing process before merging pull requests.
  
Here are changes we plan to implement in the next sprint:
   * Add logging and performance monitoring.
   * Refine UI embedding and user interaction experience.
   * We plan to meet with the client to gather feedback and identify any additional feature requests or usability improvements for the AI chatbot.
   * Based on the feedback received, we will prioritize functional enhancements or adjustments to better align the chatbot system with actual usage requirements.
