from django.urls import path

from student import views

urlpatterns = [
    path('create', views.create),
    path('get', views.get),
    path('modify', views.modify)
]