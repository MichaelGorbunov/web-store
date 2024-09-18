from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView

from students.models import Student

# Create your views here.
# students/views.py


def about(request):
    return render(request, "students/about.html")


# def contact(request):
#     return render(request, 'students/contact.html')

# def contact(request):
#     if request.method == 'POST':
#         # Получение данных из формы
#         name = request.POST.get('name')
#         message = request.POST.get('message')
#         # Обработка данных (например, сохранение в БД, отправка email и т. д.)
#         # Здесь мы просто возвращаем простой ответ
#         print(name)
#         print(message)
#         return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
#     return render(request, 'students/contact.html')

# def contacts(request):
#     return render(request, 'students/contact2.html')


def contacts(request):
    if request.method == "POST":
        # Получение данных из формы
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        print(name)
        print(phone)
        print(message)
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "students/contact2.html")


def catalogs(request):
    return render(request, "students/catalogs.html")
