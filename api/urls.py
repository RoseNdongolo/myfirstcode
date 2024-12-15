from django.urls import path
from blog import views

urlpatterns = [
    path('post/', views.get_and_post),
]