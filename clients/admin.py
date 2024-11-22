from django.contrib import admin
from .models import ClientType, Client

@admin.register(ClientType)
class ClientTypeAdmin(admin.ModelAdmin):
    """
    Админка для управления типами клиентов.
    """
    list_display = ('name', 'description')  # Поля, отображаемые в списке
    search_fields = ('name',)  # Поля для поиска по имени


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """
    Админка для управления клиентами.
    """
    list_display = ('name', 'email', 'phone', 'client_type')  # Поля для отображения в списке
    search_fields = ('name', 'email', 'phone')  # Поля для поиска
    list_filter = ('client_type',)  # Фильтрация по типу клиента
