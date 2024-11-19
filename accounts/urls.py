# accounts/urls.py
from django.urls import path
from .views import user_info_view, edit_user_info, register  # Импортируем корректную функцию edit_user_info

urlpatterns = [
    path('user/update/', edit_user_info, name='edit_user_info'),  # Заменили update_user_info на edit_user_info
    path('user/<str:username>/', user_info_view, name='user_info'),
    path('register/', register, name='register'),
]
