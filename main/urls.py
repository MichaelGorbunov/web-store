from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from main.views import contact, BlogListView, blog_item, IndexView
app_name="main"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', IndexView.as_view(),name="index"),
    path('contact/', contact,name="contact"),
    path('blog/', BlogListView.as_view(),name="blog"),
    path('blog/<int:pk>/', blog_item)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
