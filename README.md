# SBYEC Website Enhancement

## Project Summary

### One-sentence description of the project
A user-friendly and maintainable WordPress-based website enhancement for the Silver Buckle Youth Equestrian Center (SBYEC), improving event management, course pages, and social media integration.

### Additional information about the project
The **SBYEC Website Enhancement Project** aims to upgrade and complete the existing SBYEC WordPress site developed by a prior student team.  
Our focus is to improve usability, strengthen maintainability for non-technical staff, and expand missing functionalities such as:
- A **readable, staff-driven event calendar**
- Integrated **ticket purchases via Zeffy**
- Structured **lesson subpages** for Rising Stars, Private Lessons, and Group Lessons
- Improved **Facebook feed embedding** and **sponsor page management**
- **AI chatbot** for answering common questions

By project completion, the website will support a seamless user experience and efficient staff operations, reflecting SBYEC’s professionalism and community spirit.

---

## Installation

### Prerequisites
Before installation, ensure the following tools are installed:
- **Git** ≥ 2.30  
- **Docker Desktop** ≥ 4.0 (recommended for local deployment)  
- **Node.js** ≥ 18.x (optional, for frontend preview)
- **WordPress** ≥ 6.5 (running locally or on a staging server)
- **MySQL** ≥ 8.0
- **Zeffy account** (for event ticket integration)
- **Facebook Page Plugin access**

If you are testing locally, we recommend using:
- **XAMPP** (Windows/Mac) or **LocalWP** (cross-platform) for WordPress setup.

---

### Add-ons
The project leverages WordPress plugins and tools instead of Ruby gems:

| Add-on | Purpose |
|--------|----------|
| **The Events Calendar** | Manages and displays calendar events with clickable detail pages. |
| **Zeffy Integration** | Provides donation and ticket-purchase links for nonprofit events. |
| **Facebook Page Plugin** | Embeds the SBYEC Facebook feed directly on the homepage. |
| **WPForms** | Enables the “Contact Us” form and newsletter signups. |
| **Yoast SEO** | Enhances visibility and metadata optimization. |
| **AI Chatbot (optional)** | Provides automated responses to common questions. |

---

### Installation Steps

You can deploy the project locally or on a WordPress staging site.

#### Option 1: Local WordPress Setup (via XAMPP or LocalWP)
```bash
# 1. Clone this repository
git clone https://github.com/wsu-team21/SBYEC-Website-Enhancement.git
cd SBYEC-Website-Enhancement

# 2. Start local WordPress environment
# (If using XAMPP, ensure Apache & MySQL are running)
# Visit: http://localhost/phpmyadmin

# 3. Create a new database
CREATE DATABASE sbyec_db;

# 4. Move project files into your WordPress /htdocs directory
cp -r ./code/* /path/to/xampp/htdocs/sbyec

# 5. Open WordPress setup in browser
http://localhost/sbyec

# 6. Configure wp-config.php to match your database credentials
DB_NAME = 'sbyec_db'
DB_USER = 'root'
DB_PASSWORD = ''

# 7. Install required plugins
# (through WordPress dashboard → Plugins → Add New)
- The Events Calendar
- WPForms
- Facebook Page Plugin
- Zeffy Integration

# 8. Import seed data (if applicable)
Navigate to Tools → Import → WordPress → Upload `/data/seed_content.xml`

# 9. Activate theme and plugins
Appearance → Themes → Activate "SBYEC-Enhanced"
Plugins → Activate All
