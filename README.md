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


---

# Sprint 5 – Client Support, Documentation & Final Refinement

## Overview

During Sprint 5, our focus shifted from major backend architecture work to client-facing refinement and long-term maintainability.

After the cloud deployment and automation milestones achieved in Sprint 4, this sprint concentrated on ensuring that the SBYEC team could independently manage the website without ongoing developer support.

Rather than introducing major new technical systems, Sprint 5 emphasized responsiveness to client feedback, completion of requested usability improvements, and delivery of practical documentation and tutorial materials.

The main goal of this sprint was to ensure that all remaining client needs were addressed in a practical and sustainable way. This meant identifying the exact update workflows the client would need in WordPress, testing those workflows, and transforming them into clear documentation and tutorial videos.

---

## Major Updates

| Area | Description |
|------|------------|
| **Client-Guided Refinement** | Incorporated direct client feedback and questions into the final round of website support and usability improvements. |
| **Step-by-Step Manuals** | Created written instructional materials to help the client independently update important website sections without technical assistance. |
| **Tutorial Video Deliverables** | Produced walkthrough videos covering common content-management tasks requested by the client. |
| **Meet the Herd Maintenance Guide** | Documented the full workflow for adding new horses, including uploading featured images and entering descriptive content. |
| **Meet Our Team Formatting Support** | Added guidance for adjusting team-member image sizes and maintaining consistent page formatting. |
| **Sponsors & Partners Update Guide** | Created materials explaining how to add sponsor logos while preserving spacing and visual consistency. |
| **Books at the Buckle Update Instructions** | Delivered instructions for updating event images and dates so future announcements can be managed easily by the client. |
| **Chatbot UI Cleanup** | Refined the chatbot interface to improve readability and create a cleaner user-facing interaction area. |

---

## Work Summary

During this sprint, our team translated the client’s detailed questions and requests into actionable support materials.

We reviewed how several website sections were structured in WordPress, including:

- team member content and image layout 
- herd page content organization 
- sponsor logo placement and spacing 
- event announcement updates for Books at the Buckle 

A major challenge was not technical complexity itself, but determining which update workflows would be realistic for a non-technical client to perform consistently.

To address this, we tested multiple approaches inside the WordPress dashboard and selected the most stable and user-friendly methods. These workflows were then converted into concise manuals and video tutorials so that the client can independently manage future updates.

This sprint strengthened the practical value of the project by reducing reliance on the development team and improving long-term maintainability.

---

## Completion Status

All planned tasks for Sprint 5 were completed successfully.

There are no unfinished user stories or unresolved issues carried over from this sprint. The requested manuals, tutorials, and related refinements were completed, reviewed, and delivered.

---

## Key Outcome

By the end of Sprint 5, the project not only met its technical goals, but also addressed the client’s operational needs.

The website is now supported by:

- clear written documentation 
- task-specific tutorial videos 
- refined update workflows 
- improved client self-sufficiency 

This ensures the final deliverable is not only functional, but also maintainable by the organization after handoff.

---

## Reflections

Sprint 5 highlighted an important lesson in client-centered software development: a successful project is not defined only by technical implementation, but also by how usable and maintainable it is for the end client.

This sprint went well because:

- client communication was clear and productive 
- requested support materials were completed efficiently 
- team collaboration allowed documentation, testing, and recording tasks to progress smoothly 

Areas we would continue improving:

- making instructional materials even easier for non-technical users to follow 
- improving our internal validation process for documentation before final delivery

Overall, Sprint 5 served as the final refinement phase that helped align the project with the client’s real operational needs.

---

## Next Steps

Potential future follow-up work includes:

- gathering client feedback after they begin using the manuals and tutorials independently 
- expanding documentation if additional website-management tasks arise 
- making small usability refinements based on real client usage 
- continuing minor interface polish where needed 

---

## Sprint 5 Deliverables

You can watch our Sprint 5 presentation here:

[YouTube link of Sprint 5 Video](https://youtu.be/mhw-W2AJlnA)

Additional sprint-related materials and references:

- [Project Board / Completed Issues](https://github.com/users/ZY115/projects/2)
- [Frontend UI Files](https://github.com/ZY115/SBYEC/tree/main/code/frontend/src)
- [Chatbot Interface Backend](https://github.com/ZY115/SBYEC/blob/main/app.py)
- [Sprint Documentation Folder](https://github.com/ZY115/SBYEC/tree/main/docs/Reports)


---

# Sprint 6 – Final Handoff & Infrastructure Stabilization

## Overview

Sprint 6 was the project's final sprint, focused on handoff rather than new feature development.

By the end of Sprint 5, all major technical and client-facing deliverables had been completed. The chatbot was already deployed in the cloud, fully automated, and supported by initial tutorial materials. Sprint 6 therefore concentrated on finalizing the client handoff package and ensuring the deployed system would remain stable without any ongoing developer involvement.

Two streams of work defined this sprint: consolidating all tutorial videos into a single access-controlled delivery channel for the client, and resolving an unexpected infrastructure issue caused by a recent Hugging Face platform policy change.

The goal was to leave the client with a complete, self-sufficient, zero-maintenance system that would continue operating correctly after project closure.

---

## Major Updates

| Area | Description |
|------|------------|
| **Consolidated Tutorial Playlist** | Merged all Sprint 5 tutorial videos into a single YouTube playlist so the client can access every walkthrough from one link instead of tracking multiple separate videos. |
| **Unlisted Video Access** | Configured the playlist as **Unlisted**, meaning only people with the direct link can view the videos. The tutorials are not indexed, not searchable, and not publicly visible — while still free to host and easy for the client to share internally. |
| **Hugging Face Xet Storage Compatibility Fix** | Updated the daily automation pipeline to comply with Hugging Face's new Xet storage policy, which no longer permits binary files (such as `index.faiss`) to be pushed via plain `git push`. |
| **Migration from `git push` to `huggingface_hub` API** | Replaced the original `git clone` + `git push` deployment step with `huggingface_hub.HfApi.upload_folder()`, which handles Xet storage transparently and uploads both `data/` and `faiss_index/` folders in a single atomic commit. |
| **Pipeline Simplification** | As a side benefit of the rewrite, the Space now rebuilds **once per day instead of twice**, reducing redundant builds and making daily updates slightly faster and cleaner. |
| **Final Report Update** | Updated the full project report to reflect all Sprint 6 changes, including the infrastructure fix, tutorial delivery format, and the current state of the deployed system at handoff. |

---

## Work Summary

Most of the sprint was spent on handoff polish. The tutorial videos recorded in Sprint 5 were reviewed, lightly re-edited where needed, and organized into a single unlisted YouTube playlist. The unlisted setting was an intentional choice made in consultation with the client's privacy expectations: the content is effectively private to SBYEC, yet still free to host and trivial to distribute via a shared link.

The more unexpected piece of work was the infrastructure fix. Midway through the sprint we noticed that the daily automated update had stopped succeeding. Investigation revealed that Hugging Face had rolled out a storage-backend change (Xet storage), and binary files like our FAISS index (`index.faiss`) can no longer be pushed to Spaces via the traditional `git push` approach. The original deployment step in `update-content.yml`, which used `git clone` + `git push` to mirror the repository to the Hugging Face Space, was being rejected.

We replaced that step with a call to `huggingface_hub.HfApi.upload_folder()`, which is the new supported path and handles Xet uploads transparently. This restored the daily pipeline, and also allowed us to upload both the crawled text data and the FAISS index in a single commit — reducing the Space from two rebuilds per day to one.

Finally, the project report was updated to reflect the current state of the deployed system, so that the written documentation matches what the client actually has at handoff.

---

## Challenges

- The Hugging Face policy change was not announced loudly on the client-facing documentation, so the failure mode was only surfaced when the daily cron job stopped updating content. This required reading through recent Hugging Face platform release notes to identify Xet storage as the root cause.
- We had no pre-existing alerting on the automation pipeline, so the breakage was discovered passively rather than detected automatically. While we fixed the underlying issue, this highlighted a monitoring gap that would be worth addressing in any future continuation of the project.
- Consolidating videos into a single playlist required re-reviewing each tutorial for consistency (intro framing, pacing, resolution) before finalizing the playlist order.

---

## Reflections

Sprint 6 reinforced a lesson that had been quietly building across the project: the hardest part of a production system is not launching it, but keeping it running correctly when the environment around it changes.

The chatbot itself did not break this sprint. The FAISS index did not break. The Groq API did not break. What broke was an external platform's storage policy — something we had no direct control over. Having the pipeline written in a modular way (with the deployment step isolated in a single workflow file) made the fix straightforward once the root cause was identified.

The tutorial consolidation reinforced a different lesson: small client-facing refinements often matter more at handoff than large technical changes. The client does not need to know that we migrated to `upload_folder()` — but they very much appreciate having one link instead of seven.

---

## Next Steps

Since Sprint 6 is the final sprint of the project, there are no planned future sprints. However, potential follow-up work that the client or a future maintainer could pursue includes:

- Setting up a lightweight monitoring alert (email or notification) for any GitHub Actions workflow failures, so future platform changes are caught proactively rather than passively.
- Expanding the tutorial playlist if the client encounters new maintenance scenarios after handoff.
- Revisiting the chatbot's answer scope after the client has several months of real usage data to decide whether to enable broader question-answering capabilities.

---

## Sprint 6 Deliverables

You can watch our Sprint 6 presentation and full tutorial series here:

[YouTube Playlist (Unlisted) – Sprint 6 Video & Tutorials](https://www.youtube.com/watch?v=nUutb7TemQ8&list=PL7k2t_VNLHXXTMDM3oMTX-YRER4WVLoiR)

Additional sprint-related materials and references:

- [Updated Automation Workflow (`update-content.yml`)](https://github.com/ZY115/SBYEC/blob/main/.github/workflows/update-content.yml)
- [Client Tutorial – Add New Member](https://github.com/ZY115/SBYEC/blob/main/docs/Reports/ADD%20NEW%20MEMBER.pdf)
- [Client Tutorial – Edit Members](https://github.com/ZY115/SBYEC/blob/main/docs/Reports/Edit%20members.pdf)
- [Client Tutorial – MailPoet Newsletter Setup](https://github.com/ZY115/SBYEC/blob/main/docs/Reports/MailPoet.pdf)
- [Client Tutorial – Books at the Buckle Updates](https://github.com/ZY115/SBYEC/blob/main/docs/Reports/Books%20at%20the%20Buckle%20page.pdf)
- [Client Tutorial – Change Page Position / Order](https://github.com/ZY115/SBYEC/blob/main/docs/Reports/change%20position%20or%20order.pdf)
- [Final Project Report](https://github.com/ZY115/SBYEC/blob/main/docs/Reports/04_FinalReport.md)
- [Sprint Documentation Folder](https://github.com/ZY115/SBYEC/tree/main/docs/Reports)

---

## Project Summary

Over six sprints, this project evolved from a WordPress-focused website improvement effort into a complete, cloud-deployed AI chatbot system with automated content synchronization and full client handoff documentation.

The final deliverable includes:

- A custom RAG chatbot running 24/7 on Hugging Face Spaces, powered by Groq's Llama 3.3 70B model and a FAISS vector index built from the SBYEC website's own content.
- A fully automated daily update pipeline (GitHub Actions) that re-crawls the website, rebuilds embeddings, regenerates the FAISS index, and redeploys to Hugging Face — with zero manual intervention.
- A refined, accessible WordPress website with client-requested content and formatting improvements.
- A complete tutorial package (written PDFs + unlisted video playlist) enabling SBYEC staff to maintain the website independently.
- Zero ongoing cost: the entire system runs on free-tier services.

The project is now fully handed off to the client. The deployed system is stable, self-updating, documented, and does not require further developer involvement to continue operating correctly.



## Team Members
- **Yuhang Zhang** – Team Leader  
- **Richard Shen** – Developer

---

## Notes
This project is built on WordPress and focuses on improving usability, accessibility, and ease of maintenance for non-technical staff.














