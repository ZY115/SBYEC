# SBYEC Website

![SBYEC](https://raw.githubusercontent.com/ZY115/SBYEC/main/resources/1.42.16.png)


## Project Summary

An enhancement and continuation of the existing Silver Buckle Youth Equestrian Center (SBYEC) WordPress website, improving event management, usability, and maintainability for non-technical staff.

### Additional information about the project
This project continues the work of a previous WSU student team.  
The **SBYEC Website Enhancement Project** focuses on completing unfinished features, optimizing existing modules, and ensuring that SBYEC staff can independently manage and update their website.  

Key goals include:
- Restoring and upgrading the **event calendar** with Zeffy integration.  
- Completing the **lesson subpages** (Rising Stars, Private Lessons, Group Lessons).  
- Simplifying **staff content updates** via WordPress backend.  
- Improving **social media embedding**, **accessibility**, and **security (HTTPS)**.  

All development work builds upon the **existing WordPress database, content, and structure** inherited from the previous project team.


### Add-ons

| Plugin / Add-on | Purpose |
|------------------|----------|
| **The Events Calendar** | Displays and manages event calendar with detail links. |
| **Zeffy Integration** | Handles nonprofit ticketing and donations. |
| **Facebook Page Plugin** | Embeds live Facebook feed on homepage. |
| **WPForms** | Manages contact form submissions. |
| **AI Chatbot (optional)** | Provides automated FAQ responses. |
| **Yoast SEO** | SEO optimization for site visibility. |

## Sprint 1 – Preparation Phase

### Completed Tasks
- Collected client requirements.  
- Created **User Stories**, **Use Cases**, and **UML diagrams**.  
- Evaluated the existing WordPress-based system.  
- Learned about the frameworks and plugins we’ll use.  
- Started the first small round of development.


## Sprint 1 – Deliverables

### Implemented Features
- Added **individual course detail pages**.  
- Improved **page linking and navigation** across the site.  
- Added a **calendar** section.  
- Added a **schedule/timetable** section.  
- Added a **“Book Lesson”** button (redirects to contact page).  
- Added a **chatbot** for basic user interaction.

### Project Documents

- [Project Assignment 1](https://github.com/ZY115/SBYEC/blob/main/docs/Reports/Assignment%20Template.pdf)  
- [Functional Requirements](https://github.com/ZY115/SBYEC/blob/main/docs/Reports/Functional%20Requirements.pdf)
- [Meeting Agenda](https://github.com/ZY115/SBYEC/blob/main/docs/Reports/Meeting%20Agenda.pdf)
- [Meeting Minutes](https://github.com/ZY115/SBYEC/blob/main/docs/Reports/Meeting%20Minutes.pdf)
- [Project Description Team 19](https://github.com/ZY115/SBYEC/blob/main/docs/Reports/Project_Description_team19.pdf)

### Sprint 1 Demo
You can watch our Sprint 1 presentation here:  
[Watch on YouTube](https://youtu.be/OGq5JewZOqw)



### Sprint 2 – Upcoming Plans
- Fully implement the **calendar with booking and payment** features.  
- **Update team information** based on client feedback.  
- Develop and deploy a **custom chatbot** tailored to SBYEC’s needs.

## Sprint 2 – Progress Update

### Overview
During **Sprint 2**, our main focus was to complete all of the client’s required features and improve the website’s usability for non-technical staff.  
We prioritized stability and client-driven changes over new experimental features to ensure the website can be easily maintained and updated.

### Key Improvements
| Area | Description |
|-------|--------------|
| **Event Calendar** | Replaced the outdated static calendar with a **dynamic event list** powered by *The Events Calendar* plugin. Each event now includes images, description, date, time, ticket price, organizer, phone, email, and address. Events can be easily created or edited through the WordPress backend. |
| **Lesson Pages** | Updated **Rising Stars**, **Private Lessons**, and **Group Lessons** pages with richer visual content, including sample photos and embedded YouTube videos. Added test event lists for demonstration purposes. |
| **Equine Boarding & Mission Pages** | Added more photos and short videos to enhance user trust and visual appeal. These demonstrate the organization’s professional care for horses and its community mission. |
| **Client Tutorials** | Created detailed step-by-step tutorials (with screenshots) to teach SBYEC staff how to: 1) add new events, 2) edit existing events, and 3) update team members. These guides ensure long-term site maintainability. |
| **Content Structure** | Retained legacy items such as “Scholarships,” “Login,” and “Sign Up” until further client confirmation. Added a separate **All Events** page instead of replacing old content to avoid interrupting live site operations. |
| **Backend Optimization** | Simplified event-editing workflow with intuitive date/time selectors, organizer fields, and category tags. Ensured that all forms remain HTTPS-secured. |

### Challenges
Communication with the client remained the main challenge.  
Feedback on Sprint 1 changes arrived slowly, which delayed some planned updates and limited new content uploads (photos, videos, and course descriptions).  
To avoid disrupting the live site, all structural changes were made cautiously and only after receiving approval.

### Reflections
Although some media content is still missing, the overall direction and design are now aligned with the client’s vision.  
The new event list and improved page visuals significantly enhance usability and site freshness.  
Once the client provides updated course materials, the website can be quickly finalized with minimal additional work.

### Next Steps (Sprint 3 Preview)
With most mandatory tasks completed, **Sprint 3** will focus on:  
- Implementing the **custom AI chatbot** and integrating it into the website.  
- Finalizing all client tutorial materials.  
- Uploading final demo videos and documentation.

---

### Sprint 2 Deliverables
- [Solution Approach](https://github.com/ZY115/SBYEC/blob/main/docs/Reports/Solution_Approach.pdf)  
  **Modifications:**  
  Added Section VI. *Constraints and Trade-offs*  
  Added Section VII. *Standards and Constraints Verification/Testing*  
  Added reference numbers in the main text
  
- [Project Requirements and Specifications](https://github.com/ZY115/SBYEC/blob/main/docs/Reports/Project%20Requirements%20and%20Specifications_team19.pdf)  
  **Modifications:**  
  II.2. Added validation notes  
  II.3. Added UC number  
  II.5. Replaced UC number and added *Related NFR*  
  Added II.6. *Standards and Compliance*  
  Added reference numbers within the main text

- [Client Tutorial – Add New Member](https://github.com/ZY115/SBYEC/blob/main/docs/Reports/ADD%20NEW%20MEMBER.pdf)  
  Step-by-step guide for adding a new team member through the WordPress backend.

- [Client Tutorial – Edit Members](https://github.com/ZY115/SBYEC/blob/main/docs/Reports/Edit%20members.pdf)  
  Instructions for modifying or removing existing team member profiles.

- [Client Tutorial – MailPoet Newsletter Setup](https://github.com/ZY115/SBYEC/blob/main/docs/Reports/MailPoet.pdf)  
  Guide for configuring and sending newsletters using the MailPoet plugin.
  
You can watch our Sprint 2 presentation here:  
- [Watch on YouTube](https://youtu.be/F20qeLysisg)


## Sprint 3 – AI Chatbot Development

### Overview
During Sprint 3, our primary focus was the development of a fully functional, automated **AI Chatbot** tailored to SBYEC’s needs.  
Unlike traditional FAQ tools, this chatbot is built on a **Retrieval-Augmented Generation (RAG)** architecture and stays synchronized with the official SBYEC website without requiring any manual updates from staff.  

This sprint represents the most technically significant milestone of the entire project and lays the foundation for a long-term, maintenance-free intelligent assistant for SBYEC.

---

### Major Updates

| Area | Description |
|-------|--------------|
| **Automated Web Crawler** | Built a BeautifulSoup-based crawler that extracts content from 15 key SBYEC pages, including Events, Lessons, Programs, Services, and About. Automatically parses titles, text, footer information (address, phone, email), and removes irrelevant navigation elements. Produces a unified 22KB structured content file. |
| **Text Chunking & Embeddings** | Implemented 500-character text chunks with 150-character overlap using LangChain’s `RecursiveCharacterTextSplitter`. Generated 384-dimensional embeddings using the HuggingFace `all-MiniLM-L6-v2` model for efficient semantic retrieval. |
| **Vector Database (ChromaDB)** | Designed a persistent local vector store that indexes all content chunks. The chatbot retrieves the top-k relevant context entries (default k=10) for every user query. |
| **RAG Chatbot Engine** | Developed the core chatbot using Ollama’s Llama 3.2 models (1B and 3B variants). Created a custom prompt template that forces the model to rely only on retrieved SBYEC context, preventing hallucinations and ensuring factual answers. |
| **REST API Integration** | Built a Flask REST API with three endpoints: `/api/chat`, `/api/refresh`, and `/api/status`. Enabled CORS for future WordPress site integration. |
| **Auto-Refresh System** | Added an optional update checker that automatically refreshes the vector database whenever the website content changes. Also implemented a scheduled updater (daily full crawl and 6-hour events-only crawl). |
| **Frontend Demo Integration** | Created a JavaScript-based chat widget prototype. During Sprint 3, communication between the website and chatbot was enabled through an HTTPS ngrok tunnel for demonstration purposes. |

---

### Technical Architecture

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

### Key Design Decisions

- **100% automation:** Eliminates the need for SBYEC staff to manually update chatbot content.  
- **Lightweight and free:** Uses small open-source LLMs (1B) compatible with free-tier hosting.  
- **Scalable:** Can switch to a larger 3B model for higher accuracy without changing system structure.  
- **Safe and controlled:** Custom prompt rules ensure the chatbot only uses verified SBYEC content.  
- **Flexible integration:** WordPress frontend communicates with a simple JSON-based API.  

---

### Challenges

- Ensuring footer information (address, phone, email) was correctly extracted and preserved required redesigning the crawler’s parsing logic.  
- Balancing accuracy and resource usage: the 1B model fits within free hosting limits but needed tuning of chunk size, overlap, and retrieval parameters to reach high accuracy.  
- Integrating local development with a real website required secure tunneling through ngrok during the prototype phase.  

---

### Reflections

Sprint 3 successfully delivered a full, end-to-end **automated RAG chatbot system** that operates reliably on real SBYEC content.  
The system demonstrates strong performance in answering questions about contact information, programs, services, and events.  
This sprint sets up all necessary infrastructure for final deployment and production integration in the next phase.

---

### Next Steps (Sprint 4 Preview)

- Move the chatbot backend from local development to a **cloud deployment** (Railway, Render, or VPS).  
- Replace the temporary ngrok setup with a permanent HTTPS API endpoint.  
- Build a polished WordPress chat widget with error handling and optimized UI.  
- Improve retrieval accuracy for events and team member details.  
- Finalize documentation and prepare training materials for SBYEC staff.  

### Sprint 3 Deliverables
You can watch our Final presentation here(Include Sprint 3):  
- [Watch on YouTube](https://youtu.be/6_CssNaEQqY)

---

# Sprint 4 – Cloud Deployment & Production Automation

## Overview

During Sprint 4, our primary focus was transitioning the AI Chatbot from a local prototype environment into a fully cloud-deployed, production-ready system.

While Sprint 3 successfully delivered a complete RAG chatbot architecture running locally with Ollama, Sprint 4 represents a major architectural evolution:

The chatbot now runs entirely in the cloud, operates 24/7 without any local machine dependency, and maintains automatic synchronization with the live SBYEC website.

This sprint marks the transformation from a working technical prototype to a stable, automated, zero-maintenance deployment infrastructure suitable for long-term real-world use.

---

## Major Updates

| Area | Description |
|------|------------|
| **Cloud Hosting Migration** | Migrated backend from local Flask + Ollama runtime to Hugging Face Spaces (free tier, 2GB RAM). The chatbot now runs persistently in the cloud with a public URL. |
| **LLM Provider Upgrade (Groq 70B)** | Replaced local Llama 3.2 (1B/3B) with Groq’s hosted Llama 3.3 70B model via API. Achieved dramatically improved reasoning quality, coherence, and response structure. |
| **FAISS Persistent Index** | Switched from ChromaDB to a pre-built FAISS vector index stored in the repository. Reduced cold start time from database rebuild to ~1 second index load. |
| **Tiered Retrieval System** | Implemented a two-layer response system: pattern-based extraction for contact queries (no API call), and LLM invocation only when synthesis is required. |
| **GitHub Actions Automation Pipeline** | Built a fully automated daily workflow that crawls all 15 SBYEC pages, regenerates embeddings and FAISS index, commits updates, and triggers automatic Hugging Face redeployment. |
| **Production Deployment Stability** | Eliminated ngrok dependency and replaced temporary HTTPS tunneling with permanent cloud endpoint architecture. |
| **Scalable API Integration** | Prepared the system for iframe embedding or direct API-based integration into WordPress frontend. |

---

## Technical Architecture

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
├── Tier 1: Pattern Extraction (No API Call)
└── Tier 2: LLM Query (Groq 70B)
▼
Groq Llama 3.3 70B API
▼
Hugging Face Spaces Deployment
▼
Public Chat Endpoint (24/7)
```

---

## Key Improvements Over Sprint 3

### Eliminated local dependency
Sprint 3 required Ollama running continuously on a local machine.  
Sprint 4 removes all local runtime requirements. The system now operates entirely in the cloud.

### Model capability leap
Sprint 3 used Llama 3.2 (1B/3B), constrained by memory limitations.  
Sprint 4 uses Llama 3.3 70B via Groq — approximately 70× larger — resulting in significantly stronger contextual reasoning and answer fluency.

### Cold-start optimization
Sprint 3 rebuilt the vector database on startup.  
Sprint 4 loads a pre-built FAISS index instantly, improving reliability and startup speed.

### Fully automated content synchronization
Sprint 3 required manual refresh or scheduled local scripts.  
Sprint 4 implements a complete crawl → embed → index → deploy pipeline through GitHub Actions, requiring zero manual intervention.

### API usage efficiency
Tiered retrieval reduces unnecessary LLM calls, preserving free-tier API quota while maintaining accuracy.

---

## Capacity

With Groq’s free-tier limits:

- ~14,400 LLM-powered queries per day  
- ~30 requests per minute  
- Unlimited contact-information queries (handled without API calls)  

For a community organization website like SBYEC, this capacity is more than sufficient and provides significant scalability headroom.

---

## Cost

The entire deployment operates at zero cost:

- Hugging Face Spaces (free tier)  
- Groq API (free tier)  
- GitHub Actions (free for public repos)  
- Sentence-transformer embeddings (open-source, CPU-based)  

No paid infrastructure or persistent server hosting is required.

---

## Challenges

- Migrating from a local LLM runtime to a remote API required redesigning the prompt and request pipeline.
- Gemini API instability forced evaluation and comparison of multiple providers before selecting Groq.
- Free-tier constraints required careful API call budgeting and optimization.
- Ensuring that automated GitHub Actions correctly triggered Hugging Face redeployment required CI/CD debugging and workflow refinement.

---

## Reflections

Sprint 4 represents a major architectural milestone in the project lifecycle.

Sprint 3 proved the chatbot concept.  
Sprint 4 proves the chatbot can operate reliably in a real-world, production-style deployment environment.

The system is now:

- Cloud-native  
- Fully automated  
- Scalable  
- Zero-cost  
- Maintenance-free  

This sprint elevates the chatbot from a technical demo to a sustainable intelligent assistant infrastructure for SBYEC.

---

## Next Steps (Future Enhancements)

- Implement conversation memory for multi-turn contextual dialogue  
- Add analytics dashboard for query tracking  
- Improve event-specific retrieval precision  
- Add fallback logic for API outage scenarios  
- Optimize UI integration into final WordPress theme  

---

## Sprint 4 Deliverables

You can watch our Sprint 4 presentation here:

[YouTube link of Sprint 4 Video](https://youtu.be/b033JsfVcbE)


Separate Report and Code Details:

[**Project Repository**](https://github.com/ZY115/SBYEC/blob/main/docs/Reports/Sprint%204%20reports.md?plain=1)




## Team Members
- **Yuhang Zhang** – Team Leader  
- **Richard Shen** – Developer

---

## Notes
This project is built on WordPress and focuses on improving usability, accessibility, and ease of maintenance for non-technical staff.














