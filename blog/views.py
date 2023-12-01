from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.

class List(ListView):
    model = Post
    template_name = 'home.html'

class Detail(DetailView):
    model = Post
    template_name = 'detail.html'

class Create(CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['Title', 'Author', 'Body']

class Update(UpdateView):
    model = Post
    template_name = 'update.html'
    fields = ['Title', 'Body']

class Delete(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
