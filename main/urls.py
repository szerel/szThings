
from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('registration/',views.register,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('profile/',views.profile,name='profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
