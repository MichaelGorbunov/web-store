from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from main.views import contact, BlogListView, blog_item, IndexView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('contact/', contact),
    path('blog/', BlogListView.as_view()),
    path('blog/<int:pk>/', blog_item)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
