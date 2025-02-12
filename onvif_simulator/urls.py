from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^some-url-pattern/$', views.some_view, name='some_view'),
]