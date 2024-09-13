

# **CyberBot - Chatbot with News and Weather Features**

## **Project Overview**

**CyberBot** is a Django-based web application that simulates a chatbot. It provides three core functionalities:
1. General chat queries handled by the Gemini API.
2. News updates fetched from NewsAPI.
3. Weather information fetched from OpenWeatherMap API.

In addition, the application features user registration, login, profile management, and chat history storage. Users can interact with the chatbot, view past conversations, and get updates on news and weather.

## **Features**

- **User Authentication**: Users can sign up, log in, and manage their profiles.
- **Chatbot Interaction**: Users can ask general questions and receive responses powered by the Gemini API.
- **News Updates**: Get the latest news based on custom queries via NewsAPI.
- **Weather Information**: Fetch current weather details based on location via OpenWeatherMap API.
- **Chat History**: Chat conversations are stored in the database, and users can view past interactions.

## **Project Structure**

```bash
cyberbot/
│
├── chatgpt_clone/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── chat/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│   │   ├── chat/
│   │   │   ├── index.html
│   │   │   ├── chat_history.html
│   │   │   ├── login.html
│   │   │   ├── profile.html
│   │   │   ├── signup.html
│   ├── static/
│       ├── chat/
│           ├── css/
│           ├── js/
│
├── manage.py
└── requirements.txt
```

## **Installation and Setup**

### 1. **Clone the Repository**

```bash
git clone https://github.com/tashok7003/CyberBot.git
cd CyberBot
```

### 2. **Create and Activate Virtual Environment**

```bash
# Create a virtual environment
python -m venv env

# Activate the virtual environment
# For Windows:
env\Scripts\activate
# For Linux/macOS:
source env/bin/activate
```

### 3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 4. **Set Up MySQL Database**

1. Create a new MySQL database.
2. Update the `DATABASES` settings in `chatgpt_clone/settings.py` with your database credentials:

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

### 5. **Apply Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. **Create Superuser (Admin)**

```bash
python manage.py createsuperuser
```

### 7. **Run the Development Server**

```bash
python manage.py runserver
```

Open your browser and go to `http://127.0.0.1:8000/` to access the application.

### 8. **API Keys Setup**

Make sure you have your API keys for the services you’re using:

- **Gemini API** (for general chat responses)
- **NewsAPI** (for news updates)
- **OpenWeatherMap API** (for weather info)

Update the `views.py` with your respective API keys:

```python
# Gemini API
api_key = 'YOUR_GEMINI_API_KEY'

# NewsAPI
news_api_key = 'YOUR_NEWS_API_KEY'

# OpenWeatherMap
geo_api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
```

## **Usage**

1. **Sign Up/Login**: Create an account or log in.
2. **Chat**: Start interacting with the chatbot by asking general questions, requesting news updates, or weather information.
3. **Chat History**: Access your past chats from the "Chat History" section.
4. **Profile Management**: View and edit your profile information.

## **Project Features in Detail**

- **General Chat**: Users can type any general question, and responses are fetched from the Gemini API.
- **News**: When users ask for news, the chatbot fetches relevant news articles from NewsAPI.
  - **Example**: "Give me the latest news on technology."
- **Weather**: When users ask for weather information, the chatbot fetches the weather data for the specified location using OpenWeatherMap.
  - **Example**: "What’s the weather today in Bangalore?"

## **Tech Stack**

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Bootstrap for styling)
- **Database**: MySQL
- **APIs**:
  - **Gemini API**: For general chatbot responses.
  - **NewsAPI**: For fetching news updates.
  - **OpenWeatherMap API**: For fetching weather data.

## **Contributing**

Contributions are welcome! Please feel free to submit a Pull Request or raise an issue if you find any bugs or have suggestions for improvements.

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### **Contact**

- **Author**: [Ashok](https://github.com/tashok7003)
- **Project Link**: [CyberBot on GitHub](https://github.com/tashok7003/CyberBot)

---

