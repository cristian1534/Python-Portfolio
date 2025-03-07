from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('download-cv/', views.download_cv, name='download_cv'),
    path('contact/', views.contact, name='contact'),
]