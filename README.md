# Multi-Language FAQ Management System

A feature-rich FAQ management system with automatic translations, rich text editing, and API caching.

## Features ✨
- **Multi-language Support** (English, Hindi, Bengali)
- **WYSIWYG Editor** with CKEditor integration
- **Auto-translation** using Google Translate API
- **Redis-powered Caching** for API responses
- **REST API** with language parameter support
- **Admin Interface** for content management
- **HTML Sanitization** in API responses

## Installation 💻

Get started with the FAQ Management System in just a few easy steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/.git
   cd faq-management-system
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Apply database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
4. **Create Superuser:**
   ```bash
   python manage.py createsuperuser
5. **Start the server:**
   ```bash
   python manage.py runserver
6. **Start the Redis Server (Caching):**
   ```bash
   redis-server
7. **Access the system:**
   Open your browser and navigate to http://127.0.0.1:8000.

## 🛠️ Admin Panel
Access the Django admin panel at:
```
http://127.0.0.1:8000/admin/
```

## 📌 API Endpoints

### **Get FAQs (Default: English)**
```sh
GET /api/faqs/
```
Example Response:
```json
[
    {
        "id": 2,
        "question": "What is name of your College ?",
        "answer": "<p>My <em>college </em><u>name </u>is <strong>IIIT Kota</strong>.</p>"
    }
]
```

### **Get FAQs in Specific Language**
```sh
GET /api/faqs/?lang=hi
```
Example Response (Hindi):
```json
[
    {
        "id": 2,
        "question": "आपके कॉलेज का नाम क्या है?",
        "answer": "मेरे कॉलेज का नाम IIIT कोटा है।"
    }
]
```
Example Response (Bengali):
```json
[
    {
        "id": 2,
        "question": "আপনার কলেজের নাম কী?",
        "answer": "আমার কলেজের নাম iiit কোটা।"
    }
]
```
### **Create new FAQ**
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"question": "Return policy?", "answer": "<p>30-day return period</p>"}' \
  http://localhost:8000/api/faqs/
```

## 🧪 Running Tests
To run unit tests, use:
```bash
pytest
```
