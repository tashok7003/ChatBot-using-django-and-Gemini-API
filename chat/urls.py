from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),
    path('chat_history/', views.chat_history, name='chat_history'),
    path('send_message/', views.send_message, name='send_message'),
    path('load_chat/<int:chat_id>/', views.load_chat, name='load_chat'),
    path('create_chat/', views.create_chat, name='create_chat'),
    path('delete_chat/<int:chat_id>/', views.delete_chat, name='delete_chat'),
    path('get_latest_news/', views.get_latest_news, name='get_latest_news'),  # Add this line
    path('', views.index, name='index'),
]
