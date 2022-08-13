from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
<<<<<<< HEAD
    path("add_debt", views.add_debt, name="add_debt"),
    path("debt_confirm", views.debt_confirm, name="debt_confirm"),
    path("debt_sus", views.debt_sus, name="debt_sus"),
    path("sch_dir", views.sch_dir, name="sch_dir"),
    path("sch_backlog", views.sch_backlog, name="sch_backlog"),
    path("sch_contend", views.sch_contend, name="sch_contend"),
    path("sch_post", views.sch_post, name="sch_post"),
    path("sch_review", views.sch_review, name="sch_review"),
    path("contend_sus", views.contend_sus, name="contend_sus"),
=======
    path('', views.test, name='test'),
    path("add_debt/", views.add_debt, name="add_debt"),
    path("debt_confirm/", views.debt_confirm, name="debt_confirm"),
    path("debt_sus/", views.debt_sus, name="debt_sus"),
    path("sch_dir/", views.sch_dir, name="sch_dir"),
    path("sch_backlog/", views.sch_backlog, name="sch_backlog"),
    path("sch_contend/", views.sch_contend, name="sch_contend"),
    path("sch_post/", views.sch_post, name="sch_post"),
    path("sch_comment/<str:pk>/", views.sch_comment, name="sch_comment"),
    path("sch_review/", views.sch_review, name="sch_review"),
    path("contend_sus/", views.contend_sus, name="contend_sus"),
>>>>>>> 4d57127d363dcd0ca262a70346a3046b12a3d837

    path("gdn_clear/", views.gdn_clear, name="gdn_clear"),
    path("gdn_confirm/", views.gdn_confirm, name="gdn_confirm"),
    path('chd_form/', views.guardian_add_child_page, name='chd_form'),
    path("gdn_contend/", views.gdn_contend, name="gdn_contend"),

]
