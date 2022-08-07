from django.urls import path
from . import views

urlpatterns = [
    path('landing/', views.landing_page, name='landing'),
    path('school_registered/', views.school_reg_page, name='school_registered'),
    path('contact_us/', views.contact_us_page, name='contact_us'),
]
