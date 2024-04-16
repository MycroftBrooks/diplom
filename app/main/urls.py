from django.urls import path

from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("hello/", views.index, name="hello"),
    path("support/", views.support, name="support"),
    path("treaty/<int:id>", views.detail_treaty, name="detail_treaty"),
    path("treaty/record/create/<int:id>", views.create_record, name="create_record"), # id of treaty
    path("treaty/record/delete/<int:id>", views.delete_record, name="delete_record"), # id of record
    path("treaty/create", views.create_treaty, name="create_treaty"),
    path("treaty/delete/<int:id>", views.delete_treaty, name="delete_treaty"),
    path('register/', views.register_user, name="register"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('', views.main, name='')
]
""" if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) """