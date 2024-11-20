from django.urls import path
from . import views

urlpatterns = [
    path('display_tables/', views.display_tables, name='display_tables'),
]
