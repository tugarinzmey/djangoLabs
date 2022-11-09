from django.shortcuts import HttpResponse, render
from .forms import UserForm

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        basket = request.POST.get("basket")
        sochi = request.POST.get("sochi")
        email = request.POST.get("email")
        url = request.POST.get("url")
        file_path = request.POST.get("file_path")
        choosed_file = request.POST.get("choose_file")

        output = "<div><h2>Пользователь {0}</h2><h3>Возраст: {1}</h3><h3>{2}</h3><h3>Сочи: {3}</h3><h3>Эл. почта: {4}</h3><h3>Ссылка: {5}</h3><h3>Путь к файлу: {6}</h3><h3>{7}</h3><div>".format(name, age, basket, sochi, email, url, file_path, choosed_file)
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})

def about(request):
    return HttpResponse("<h2>О сайте<h2>")

def contact(request):
    return HttpResponse("<h2>Контакты<h2>")

def products(request, productId = 1):
    output = "<h2>Продукт №{0}</h2>".format(productId)
    return HttpResponse(output)

def users(request, id = 1, name = "Леха"):
    output = "<div><h2>Пользователь</h2> <h3>id: {0} Имя: {1}</h3><div>".format(id, name)
    return HttpResponse(output)