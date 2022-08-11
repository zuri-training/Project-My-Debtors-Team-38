from django.contrib import admin
from django.urls import path
from . import views


app_name = "accounts"


urlpatterns = [
    # log in and reg
    path('select_reg/', views.select_reg_page, name='select_reg'),
    path('login/', views.login_page, name='login'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),

    # school
    path('sch_reg/', views.school_register_page, name='sch_reg'),
    path('sch_dshbd/', views.school_dashboard_page, name='sch_dshbd'),

    # guardian
    path('gdn_reg/', views.guardian_register_page, name='gdn_reg'),
    path('gdn_wlc/', views.guardian_home_page, name='gdn_wlc'),

]
