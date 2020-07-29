from django.urls import path

from .views import HomeView, CreateKintore

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('create', CreateKintore.as_view(), name='create')
]