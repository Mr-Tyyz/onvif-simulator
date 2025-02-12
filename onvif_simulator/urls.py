from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.some_view, name='some_view'),
    re_path(r'^camera/(?P<pk>\d+)/$', views.camera_view, name='camera_view'),
]