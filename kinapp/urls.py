from django.urls import path

from .views import HomeView, CreateKintore, UpdateKintore, DeleteKintore

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('create', CreateKintore.as_view(), name='create'),
    path('update/<int:pk>', UpdateKintore.as_view(), name='update'),
    path('delete/<int:pk>', DeleteKintore.as_view(), name='delete'),
]