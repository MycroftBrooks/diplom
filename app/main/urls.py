from django.urls import path

from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("hello/", views.index, name="hello"),
    path("support/", views.support, name="support"),
    path('register/', views.register_user, name="register"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('', views.main, name='')
]
""" if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) """