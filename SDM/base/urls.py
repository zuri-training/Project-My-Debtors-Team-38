from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('home/', views.landing_page, name='home'),
    path('school_registered/', views.school_list_page, name='school_registered'),
    path('contact_us/', views.contact_us_page, name='contact_us'),
]
