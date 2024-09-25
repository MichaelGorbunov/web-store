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
    path("product_detail/<int:product_id>/", views.product_detail, name="product_detail"),
    path("products_list/", views.products_list, name="products_list"),
    path("detail/<int:product_id>/", views.detail, name="detail"),
    path('articles/', views.articles_list, name='articles_by_page'),
    path('add_product/', views.add_product, name='add_product'),

]
