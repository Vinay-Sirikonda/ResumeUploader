from django.contrib import admin
from django.conf.urls import url
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url('admin/', admin.site.urls),
    url('', views.HomeView.as_view(), name='home'),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)