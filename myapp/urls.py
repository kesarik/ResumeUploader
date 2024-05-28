from django.contrib import admin
from django.urls import path, include
from .views import homeview  
from .views import CandidateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeview.as_view(), name='home'),
    path('<int:pk>/', CandidateView.as_view(), name='candidate'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
