from django import forms
from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Введите имя")
    age = forms.IntegerField(label="Введите возраст")
    basket = forms.BooleanField(label="Положить товар в корзину?")
    sochi = forms.NullBooleanField(label="Вы поедете в Сочи?")
    email = forms.EmailField(label="Введите email")
    url = forms.URLField(label="Введите ссылку")
    file_path = forms.FilePathField(label="Укажите путь к файлу", path=r"C:\Users\Mark\Desktop\djangoLabs\labs\labsApp")
    choosed_file = forms.FileField(label="Выберите файл")