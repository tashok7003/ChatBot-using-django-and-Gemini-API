---

# 🤖 **CyberBot – AI Chatbot with News & Weather Intelligence**

[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.x-darkgreen)](https://www.djangoproject.com/)
[![MySQL](https://img.shields.io/badge/Database-MySQL-orange)](https://www.mysql.com/)
[![Gemini API](https://img.shields.io/badge/API-Gemini-blueviolet)](https://ai.google.dev/)
[![NewsAPI](https://img.shields.io/badge/API-NewsAPI-red)](https://newsapi.org/)
[![OpenWeather](https://img.shields.io/badge/API-OpenWeatherMap-lightblue)](https://openweathermap.org/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](#)
[![Status](https://img.shields.io/badge/Status-Active-success)](#)

---

## 🚀 **Project Overview**

**CyberBot** is a Django-based AI chatbot that provides:

1. **General Chat Responses** using the **Gemini API**
2. **Real-Time News Updates** using **NewsAPI**
3. **Weather Information** using **OpenWeatherMap**

Along with this, users can create accounts, manage profiles, and view previous chat history.
The system serves as a complete AI-powered chatbot with multi-feature integration.

---

## ⭐ **Key Features**

### 🔐 User System

* Secure registration & login
* Profile management
* Personalized chat space
* Stored chat history

### 🤖 Chatbot Features

* General AI responses via Gemini API
* Technology, business, world news & custom queries
* Real-time weather updates by location

### 🗂️ Chat History

* Stores all previous conversations
* Users can revisit and view past chats

---

## 📁 **Project Structure**

```bash
cyberbot/
│
├── chatgpt_clone/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── chat/
│   ├── admin.py
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│
│   ├── templates/chat/
│   │   ├── index.html
│   │   ├── chat_history.html
│   │   ├── login.html
│   │   ├── profile.html
│   │   ├── signup.html
│
│   ├── static/chat/
│       ├── css/
│       ├── js/
│
├── manage.py
└── requirements.txt
```

---

## ⚙️ **Installation & Setup**

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/tashok7003/CyberBot.git
cd CyberBot
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv env
env\Scripts\activate       # Windows
source env/bin/activate    # Linux / macOS
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure MySQL Database

Update `DATABASES` in `chatgpt_clone/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create Admin User

```bash
python manage.py createsuperuser
```

### 7️⃣ Start the Development Server

```bash
python manage.py runserver
```

Visit: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🔑 **API Keys Setup**

Add your API keys inside `views.py`:

```python
# Gemini API
api_key = 'YOUR_GEMINI_API_KEY'

# NewsAPI
news_api_key = 'YOUR_NEWS_API_KEY'

# OpenWeatherMap
geo_api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
```

---

## 🧠 **Usage Guide**

### 📝 Steps:

1. **Create Account / Login**
2. Ask questions like:

   * “Explain quantum computing”
   * “Latest news on AI”
   * “Weather in Bangalore”
3. View your **Chat History**
4. Update your **Profile Information**

---

## 🛰️ **Tech Stack**

| Component | Technology                   |
| --------- | ---------------------------- |
| Backend   | Django (Python)              |
| Frontend  | HTML, CSS, JS, Bootstrap     |
| Database  | MySQL                        |
| APIs      | Gemini, NewsAPI, OpenWeather |


---

## 📬 Contact

**Author:** Ashok
🔗 GitHub: [https://github.com/tashok7003](https://github.com/tashok7003)
📌 Project Link: [https://github.com/tashok7003/CyberBot](https://github.com/tashok7003/CyberBot)

---
