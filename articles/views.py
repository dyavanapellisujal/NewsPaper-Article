from typing import Any, Dict, Optional
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Articles, Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import commentsform
from django.views import View
from django.urls import reverse

# from django import

from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin


class ArticleNewView(LoginRequiredMixin, CreateView):
    model = Articles
    template_name = "article_new.html"
    success_url = reverse_lazy("articleslist")
    fields = (
        "title",
        "body",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentGet(DetailView):
    model = Articles
    template_name = "articles_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = commentsform()
        return context


class Commentpost(SingleObjectMixin, FormView):
    model = Articles
    form_class = commentsform
    template_name = "articles_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        article = self.get_object()
        return reverse("articles_detail", kwargs={"pk": article.pk})


class ArticleListView(LoginRequiredMixin, ListView):
    model = Articles
    template_name = "articleslist.html"


class ArticleDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = Commentpost.as_view()
        return view(request, *args, **kwargs)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articles
    fields = ("title", "body")
    template_name = "article_update.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articles
    success_url = reverse_lazy("articleslist")
    template_name = "articles_delete.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


# Create your views here.
