from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('school_reg_with_us/', views.school_reg_page, name='school_reg_with_us'),
    path('contact_us_form/', views.contact_us_page, name='contact_us_form'),
]
