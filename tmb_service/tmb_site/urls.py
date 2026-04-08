from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('galerie/', views.galerie, name='galerie'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('modele/<int:modele_id>/', views.modele_detail, name='modele_detail'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('like/<int:modele_id>/', views.toggle_like, name='toggle_like'),
    path('comment/<int:modele_id>/', views.add_comment, name='add_comment'),
]