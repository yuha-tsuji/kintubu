from django.shortcuts import render
from django.views.generic import ListView

from .models import KintoreModel

# Create your views here.

class HomeView(ListView):
	template_name='home.html'
	model = KintoreModel