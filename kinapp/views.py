from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import KintoreModel

# Create your views here.

class HomeView(ListView):
	template_name='home.html'
	# model = KintoreModel

	def get(self, request):
		qs = KintoreModel.objects.filter(user=request.user)
		return render(request, self.template_name, {'objectsList': qs})

class CreateKintore(CreateView):
	template_name = 'create.html'
	model = KintoreModel
	fields = ('bui', 'menu', 'kaisu', 'setsu')
	success_url = reverse_lazy('home')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class UpdateKintore(UpdateView):
	template_name = 'update.html'
	model = KintoreModel
	fields = ('bui', 'menu', 'kaisu', 'setsu')
	success_url = reverse_lazy('home')

class DeleteKintore(DeleteView):
	template_name = 'home.html'
	model = KintoreModel
	success_url = reverse_lazy('home')