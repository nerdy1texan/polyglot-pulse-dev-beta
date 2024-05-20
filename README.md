## App Structure

PolyGlotPulse/
├── media/
├── PolyGlotPulse/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       ├── guildhawk.ico
│       ├── guildhawk_logo.png
├── summarizer/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   ├── models.py
│   ├── templates/
│   │   ├── registration/
│   │   │   ├── login.html
│   │   │   ├── signup.html
│   │   ├── base.html
│   │   ├── history.html
│   │   ├── home.html
│   │   ├── summarize.html
│   │   ├── summary.html
│   │   └── upload.html
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── venv/
├── .env
├── .gitignore
├── db.sqlite3
├── guildhawk_favicon.jpg
├── guildhawk_logo.svg
├── manage.py
├── README.md
├── requirements-dev.txt
└── requirements.txt


# PolyGlot Pulse

PolyGlot Pulse is a Django-based web application that allows users to upload documents and generate summaries using the OpenAI API.

## Features

- User Authentication (Sign Up, Login, Logout)
- Document Upload (Supports multiple formats)
- Summary Generation with word count and tone customization
- History of generated summaries

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone <repository_url>
   cd PolyGlotPulse
# en-doc-summarizer
