# SBYEC Website Enhancement

## Project Summary

### One-sentence description of the project
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

---

## Installation

### Prerequisites
Before proceeding, make sure you have the following installed:
- **Git** ≥ 2.30  
- **WordPress** ≥ 6.5 (either local or hosted)  
- **PHP** ≥ 8.0  
- **MySQL** ≥ 8.0  
- **Docker Desktop** (optional, for local deployment)  
- **XAMPP** or **LocalWP** (for local environment)
- **Zeffy account** and **Facebook Page access** (for event and feed integration)

---

### Add-ons
Since the system runs on WordPress, these plugins (not Ruby gems) are essential:

| Plugin / Add-on | Purpose |
|------------------|----------|
| **The Events Calendar** | Displays and manages event calendar with detail links. |
| **Zeffy Integration** | Handles nonprofit ticketing and donations. |
| **Facebook Page Plugin** | Embeds live Facebook feed on homepage. |
| **WPForms** | Manages contact form submissions. |
| **AI Chatbot (optional)** | Provides automated FAQ responses. |
| **Yoast SEO** | SEO optimization for site visibility. |

---

### Installation Steps 

Since this project inherits the **existing SBYEC WordPress site and database**, you only need to restore and connect to the previous environment.

```bash
# 1. Clone this repository (code continuation)
git clone https://github.com/wsu-team21/SBYEC-Website-Enhancement.git
cd SBYEC-Website-Enhancement

# 2. Obtain previous team's WordPress package and database
#    (Typically shared by client as .zip and .sql files)
#    Example:
#    - wordpress_files.zip
#    - sbyec_db.sql

# 3. Restore the WordPress files
unzip wordpress_files.zip -d /path/to/xampp/htdocs/sbyec

# 4. Import the previous database
#    Use phpMyAdmin or MySQL CLI:
mysql -u root -p
> CREATE DATABASE sbyec_db;
> USE sbyec_db;
> SOURCE /path/to/sbyec_db.sql;

# 5. Configure database connection
Edit /sbyec/wp-config.php:
define('DB_NAME', 'sbyec_db');
define('DB_USER', 'root');
define('DB_PASSWORD', '');

# 6. Start the local environment
# For XAMPP users:
# - Start Apache and MySQL
# - Open browser: http://localhost/sbyec

# 7. Verify plugins are active
# WordPress Dashboard → Plugins → Ensure Events Calendar, WPForms, Zeffy are active.

# 8. (Optional) Import seed content if needed
# Navigate to Tools → Import → WordPress → Upload `seed_content.xml`
