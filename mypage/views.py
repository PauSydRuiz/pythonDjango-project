from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post
# Create your views here.
# def dashboard(request):
#   return render(request, 'dashboard.html',{})

class DashboardView(ListView):
  model = Post
  template_name = 'dashboard.html'
  

class Detail(DetailView):
  model = Post
  template_name = 'detail.html'
  