"""ChatServerPlayground URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


app_name = "accounts"


urlpatterns = [
    # log in and reg
    path('select_reg/', views.select_reg_page, name='select_reg'),
    path('login/', views.login, name='login'),

    # school
    path('sch_reg/', views.school_register_page, name='sch_reg'),
    path('sch_dshbd/', views.school_dashboard_page, name='sch_dshbd'),

    # guardian
    path('gdn_reg/', views.guardian_register_page, name='gdn_reg'),
    path('chd_form/', views.guardian_add_child_page, name='chd_form'),
    path('gdn_wlc/', views.guardian_home_page, name='gdn_wlc'),
]
