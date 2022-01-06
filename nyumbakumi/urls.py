from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/register/', views.registration, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)