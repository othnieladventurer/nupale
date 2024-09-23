from django.urls import path
from . import views






app_name= 'nupale'

urlpatterns = [
    path('', views.index, name="index"),

    path('career/', views.career, name="careers"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('request-a-demo/', views.quote, name="quote"),
    path('privacy-policy/', views.privacy_policy, name="privacy"),
    path('terms-of-use/', views.terms, name="terms"),

]



