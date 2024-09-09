from django.shortcuts import render

# Create your views here.
# students/views.py


def about(request):
    return render(request, 'students/about.html')

def contact(request):
    return render(request, 'students/contact.html')