from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.template import loader
from django.urls import reverse_lazy
from .models import Product, Category

class ProductListView(ListView):

    model = Product
    paginate_by = 100

class DetailView(DetailView):
    model = Product
    template_name = 'polls/detail'

class UpdateView(UpdateView):
    model = Product
    fields = ['name']
    template_name_suffix = 'polls/update'

class DeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('delete')



