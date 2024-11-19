from django import forms
from django.contrib.auth.models import User
from clients.models import ClientType
from .models import UserInfo

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Подтвердите пароль")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Этот email уже зарегистрирован.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают.")
        
        return cleaned_data

class UserInfoForm(forms.ModelForm):
    phone = forms.CharField(max_length=20, required=False, label="Телефон")
    address = forms.CharField(max_length=255, required=False, label="Адрес")
    client_type = forms.ModelChoiceField(queryset=ClientType.objects.all(), required=True, label="Тип клиента")

    class Meta:
        model = UserInfo
        fields = ['phone', 'address', 'client_type']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры.")
        return phone

    def clean_client_type(self):
        client_type = self.cleaned_data.get('client_type')
        if not client_type:
            raise forms.ValidationError("Выберите тип клиента.")
        return client_type
