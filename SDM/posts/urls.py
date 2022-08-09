from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path("add_debt", views.add_debt, name="add_debt"),
    path('contend_sus', views.contend_sus, name="contend_sus")
]
