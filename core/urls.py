from django.urls import path
from .import views


urlpatterns = [
    path('',views.home, name='home'),
    path('contact/<int:id>/', views.contact_detail, name='contact_detail'),
]