import json
import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import ChatMessage
import logging
import re


logger = logging.getLogger(__name__)

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'chat/signup.html'

class CustomLoginView(LoginView):
    template_name = 'chat/login.html'

@login_required
def profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'chat/profile.html', {'form': form})

@login_required
def chat_history(request):
    chats = ChatMessage.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'chat/chat_history.html', {'chats': chats})

@login_required
def index(request):
    return render(request, 'chat/index.html')

@login_required
def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message')
        chat_id = data.get('chat_id')
        session_name = data.get('session_name', '')  

        if 'news' in message.lower() or 'brief' in message.lower():
            response_text = fetch_latest_news(message)
        elif 'weather' in message.lower():
            location = extract_location_from_message(message)
            response_text = get_weather(location)
        else:
            response_text = get_gemini_response(message)

        if chat_id:
            try:
                chat_message = ChatMessage.objects.get(id=chat_id, user=request.user)
                chat_message.message = f"{chat_message.message}\n{message}"
                chat_message.response = f"{chat_message.response}\n{response_text}"
                chat_message.save()
            except ChatMessage.DoesNotExist:
                return JsonResponse({'error': 'Chat not found'}, status=404)
        else:
            if not session_name:
                session_name = message[:50]  
            chat_message = ChatMessage.objects.create(
                user=request.user,
                session_name=session_name,  
                message=message,
                response=response_text
            )

        return JsonResponse({'response': response_text, 'chat_id': chat_message.id})

def extract_location_from_message(message):
    words = message.split()
    location_index = words.index('in') + 1 if 'in' in words else -1
    if location_index != -1 and location_index < len(words):
        return ' '.join(words[location_index:])
    return 'India'

def get_gemini_response(message):
    api_key = 'AIzaSyB4NIuct2DyFSqwHg4wXg2_eziLI1R6MVI'
    url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        'contents': [
            {
                'parts': [
                    {'text': message}
                ]
            }
        ]
    }
    params = {
        'key': api_key
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, params=params)
        response.raise_for_status()
        response_data = response.json()
        response_text = response_data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', 'No response field in API response')
        
        # Format bold text
        response_text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<b>\1</b>', response_text)  
        response_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', response_text)     
        return response_text.replace('\n', '<br>')
    except requests.RequestException as e:
        logger.error(f"Error making API request: {e}")
        return 'Sorry, something went wrong with the chat service.'

@login_required
def load_chat(request, chat_id):
    try:
        chat_message = ChatMessage.objects.get(id=chat_id, user=request.user)
        messages = []
        user_messages = chat_message.message.split('\n')
        bot_responses = chat_message.response.split('\n')
        for idx, user_message in enumerate(user_messages):
            messages.append({'id': len(messages) + 1, 'sender': 'user', 'text': user_message})
            if idx < len(bot_responses):
                messages.append({'id': len(messages) + 1, 'sender': 'bot', 'text': bot_responses[idx]})
        return JsonResponse({
            'messages': messages,
            'session_name': chat_message.session_name
        })
    except ChatMessage.DoesNotExist:
        return JsonResponse({'error': 'Chat not found'}, status=404)

@login_required
def create_chat(request):
    if request.method == 'POST':
        chat_message = ChatMessage.objects.create(
            user=request.user,
            message='',
            response=''
        )
        return JsonResponse({'chat_id': chat_message.id})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@login_required
def delete_chat(request, chat_id):
    if request.method == 'POST':
        try:
            chat_message = ChatMessage.objects.get(id=chat_id, user=request.user)
            chat_message.delete()
            return JsonResponse({'success': True})
        except ChatMessage.DoesNotExist:
            return JsonResponse({'error': 'Chat not found'}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@login_required
def get_latest_news(request):
    query = request.GET.get('query', 'latest news')
    news_text = fetch_latest_news(query)
    return JsonResponse({'news': news_text})

def extract_keywords(query):
    stop_words = ['news', 'about', 'this', 'the', 'and', 'or']
    keywords = ' '.join([word for word in query.split() if word.lower() not in stop_words])
    return keywords

def fetch_latest_news(query):
    api_key = 'c882f547d2bf47dfa826d16e4cc7df33'
    url = 'https://newsapi.org/v2/everything'
    keywords = extract_keywords(query)
    params = {
        'q': keywords,
        'sortBy': 'popularity',
        'apiKey': api_key
    }

    try:
        logger.debug(f"Sending request to News API with params: {params}")  

        response = requests.get(url, params=params)
        response.raise_for_status()
        news_data = response.json()

        logger.debug(f"News API response: {news_data}")  

        news_articles = news_data.get('articles', [])

        if news_articles:
            news_text = ''
            for article in news_articles:
                news_text += f"<b>{article['title']}</b><br>{article['description']}<br><a href='{article['url']}'>Read more</a><br><br>"
            return news_text

        return f'No news articles found for your query: {keywords}.'
    except requests.RequestException as e:
        logger.error(f"Error fetching news: {e}")
        return 'Sorry, something went wrong with the news service.'

def get_weather(location):
    geo_api_key = '73f5b440f2a56843bc99d32e0877df7d'
    geo_url = 'http://api.openweathermap.org/geo/1.0/direct'
    params = {
        'q': location,
        'limit': 1,
        'appid': geo_api_key
    }

    try:
        geo_response = requests.get(geo_url, params=params)
        geo_response.raise_for_status()
        geo_data = geo_response.json()

        if not geo_data:
            return f'No geolocation data found for: {location}.'

        lat = geo_data[0]['lat']
        lon = geo_data[0]['lon']

        weather_url = 'https://api.openweathermap.org/data/2.5/weather'
        weather_params = {
            'lat': lat,
            'lon': lon,
            'appid': geo_api_key,
            'units': 'metric' 
        }

        weather_response = requests.get(weather_url, params=weather_params)
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        logger.debug(f"Weather API response: {weather_data}") 

        if 'weather' in weather_data:
            description = weather_data['weather'][0]['description'].capitalize()
            temperature = weather_data['main']['temp']
            city = geo_data[0]['name']
            weather_text = f"The current weather in {city} is {description} with a temperature of {temperature}°C."
            return weather_text

        return f'No weather information found for your query: {location}.'
    except requests.RequestException as e:
        logger.error(f"Error fetching weather: {e}")
        return 'Sorry, something went wrong with the weather service.'
