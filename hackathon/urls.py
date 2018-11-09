from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_news, name='post_news'),
]
