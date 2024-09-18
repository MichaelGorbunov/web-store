# students/urls.py
from django.urls import path

from students import views

urlpatterns = [
    path("about/", views.about, name="about"),
    # path('contact/', views.contact, name='contact'),
    path("contacts/", views.contacts, name="contacts"),
    path("catalogs/", views.catalogs, name="catalogs"),
    path("", views.contacts, name="catalogs"),
]
