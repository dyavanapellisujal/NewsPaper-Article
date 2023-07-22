from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleNewView,
)


urlpatterns = [
    path("", ArticleListView.as_view(), name="articleslist"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="articles_detail"),
    path("<int:pk>/edit", ArticleUpdateView.as_view(), name="articles_edit"),
    path("<int:pk>/delete", ArticleDeleteView.as_view(), name="articles_delete"),
    path("new/", ArticleNewView.as_view(), name="articles_new"),
]
