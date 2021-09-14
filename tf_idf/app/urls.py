from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('upload/table/', views.table, name='table')
]
