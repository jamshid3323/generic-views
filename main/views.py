from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView
from .models import BooksModel
from .form import CreateBookForm


# class HomeView(TemplateView):
#     template_name = 'main/index.html'


class ObjectView(ListView):
    # model = BooksModel
    # queryset = BooksModel.objects.all().filter(name='Xitoy')
    template_name = 'main/index.html'

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            qs = BooksModel.objects.all().filter(name__icontains=q)
        else:
            qs = BooksModel.objects.all()
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        q = self.request.GET.get('q')
        if q:
            context['q'] = q
        return context


class CreateBookView(CreateView):
    model = BooksModel
    # fields = ['name', 'price']
    success_url = '/'
    template_name = 'main/form.html'
    form_class = CreateBookForm


class UpdateBookView(UpdateView):
    model = BooksModel
    fields = ['name', 'price']
    template_name = 'main/update.html'
    success_url = '/'


class BookDetailView(DetailView):
    model = BooksModel
    template_name = 'main/detail.html'