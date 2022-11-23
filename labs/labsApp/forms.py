from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.forms import PasswordInput, ModelForm
from django.core.validators import validate_email


class UserForm(forms.Form):
    name = forms.CharField(label="Введите имя")
    age = forms.IntegerField(label="Введите возраст")
    basket = forms.BooleanField(label="Положить товар в корзину?")
    sochi = forms.NullBooleanField(label="Вы поедете в Сочи?")
    email = forms.EmailField(label="Введите email")
    url = forms.URLField(label="Введите ссылку")
    file_path = forms.FilePathField(label="Укажите путь к файлу", path=r"C:\Users\Mark\Desktop\djangoLabs\labs\labsApp")
    choosed_file = forms.FileField(label="Выберите файл")

class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Username')
    password = forms.CharField(required=True, label='Пароль')

class RegisterForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']

    username = forms.CharField(min_length=3, max_length=10, required=True, label='Никнейм', validators=[
        RegexValidator(
            regex='^[a-zA-Z0-9]*$',
            message='Может содержать только латинские буквы и цифры',
            code='invalid_username'
        ),
    ])

    email = forms.CharField(min_length=3, required=True, label='Email')

    password = forms.CharField(widget=PasswordInput(), required=True, label='Пароль')
    password_confirm = forms.CharField(widget=PasswordInput(), required=True, label='Повторите пароль')

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password != password_confirm:
            raise forms.ValidationError(
                {'password_confirm': "Пароли не совпадают", 'password': ''}
            )
        # валидация никнейма
        username = self.cleaned_data.get("username")

        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError({'username': "Такой логин уже занят"})

        # валидация email
        try:
            validate_email(self.cleaned_data.get("email"))
        except ValidationError as e:
            raise forms.ValidationError({'email': "Email не является валидным адресом"})

        return cleaned_data
