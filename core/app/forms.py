from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserCreateForm(UserCreationForm):
    """
    Форма для правильного отображения порядка выводимых полей
    extra_data должно быть снизу, после обязательных полей
    """
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput)
    extra_data = forms.CharField(label="Дополнительные данные в расширенной модели", widget=forms.Textarea, required=False)
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "extra_data")


class UserUpdateForm(forms.ModelForm):
    """
    Форма изменения логина и дополнительной информации пользователя
    """
    extra_data = forms.CharField(label="Дополнительные данные в расширенной модели", widget=forms.Textarea, required=False)
    class Meta:
        model = User
        fields = ("username", "extra_data")

