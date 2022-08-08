from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.test, name='test'),
    path("add_debt", views.add_debt, name="add_debt"),
]
