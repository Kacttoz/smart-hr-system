# Offer Letter Generation System

A comprehensive automated system for generating and emailing professional offer letters. Built with Django, this application streamlines the HR process by allowing administrators to generate PDF offer letters from templates, preview them, and email them directly to candidates.

## 🚀 Features

*   **Role-Based Access Control (RBAC):**
    *   **Main Admin:** Full blocking/unblocking of sub-admins, view all letters.
    *   **Sub Admin:** Generate letters, view their own history.
*   **Automated Document Generation:**
    *   Generates DOCX from a standard template (`appointment_template.docx`).
    *   Converts DOCX to PDF automatically.
    *   **Smart Formatting:** Auto-bolds candidate details, handles salary-in-words conversion.
*   **Email Integration (SMTP):**
    *   Sends professional emails with the PDF offer letter attached.
    *   Customizable email templates with dynamic fields (Name, Position, Portal ID).
    *   Supports Gmail and Custom Domain SMTP (e.g., Hostinger).
*   **Preview Mode:**
    *   Preview the generated PDF in the browser before sending.
    *   Validation without saving "Draft" junk to the database.
*   **Dashboard & Analytics:**
    *   Track status of letters (Sent/Draft/Failed).
    *   Download historically generated letters.

## 🛠️ Technology Stack

*   **Backend:** Python 3.x, Django 5.x
*   **Database:** SQLite (Default) / MySQL (Compatible)
*   **Frontend:** HTML5, TailwindCSS (for styling)
*   **Document Processing:** 
    *   `docxtpl` (Templating)
    *   `docx2pdf` (PDF Conversion)
    *   `python-docx` (Layout corrections)
*   **Email:** Django SMTP Backend

## ⚙️ Installation & Setup

### Prerequisites
*   Python 3.10+ installed.
*   Microsoft Word installed (Required for `docx2pdf` conversion).

### 1. Clone & Install
```bash
# Clone the repository
git clone <repository_url>
cd <project_folder>

# Create Virtual Environment
python -m venv venv
.\venv\Scripts\activate   # Windows

# Install Dependencies
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Create a `.env` file in the root directory and add the following:

```env
DEBUG=True
SECRET_KEY=your-secret-key
# Database (Optional, defaults to SQLite)
# DB_NAME=...
# DB_USER=...

# Email Configuration (Hostinger Example)
EMAIL_HOST=smtp.hostinger.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=hr@kactto.com
EMAIL_HOST_PASSWORD=your_password_here
```

### 3. Run Migrations & Server
```bash
python manage.py migrate
python manage.py createsuperuser  # Create Main Admin
python manage.py runserver
```

## 📖 Usage Guide

1.  **Login:** Access `http://127.0.0.1:8000/` and login with Admin credentials.
2.  **Dashboard:**
    *   **Main Admin:** Manage Sub-Admins in the 'Manage Users' section.
    *   **Sub Admin:** Click **"Generate New Letter"**.
3.  **Generate Letter:**
    *   Fill in Candidate Name, Gender, Position, Salary, Joining Date.
    *   **Preview:** Click "Preview" to see the PDF without sending.
    *   **Send:** Click "Generate & Send" to email the candidate.
4.  **History:** View and download past letters from the dashboard table.

## 📝 Template Customization
To modify the letter format, edit `letters/appointment_template.docx`. Ensure Jinja2 tags like `{{ candidate_name }}` are preserved.

---
**Developed for Kactto HR Team**
