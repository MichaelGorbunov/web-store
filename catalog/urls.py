# students/urls.py
from django.urls import path

from catalog import views
# from catalog.views import home,contact,send
app_name = 'catalog'

urlpatterns = [
    # path("contact/", views.about, name="about"),
    path('contact/', views.contact, name='contact'),
    path("home/", views.home, name="home"),
    # path("", views.contacts, name="catalogs"),
    # path("index/<int:student_id>/", views.index, name="index"),
    path("send/", views.send, name="send"),
    path("product_detail/", views.product_detail, name="product_detail"),
    path("products_list/", views.products_list, name="products_list"),
]
