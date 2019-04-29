from django.contrib import admin
from django.urls import path

from catalog.views import BookDetailView, BookListView, PublisherDetailView, list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/<int:pk>', BookDetailView.as_view()),
    path('book/', BookListView.as_view()),
    path('publisher/<int:pk>', PublisherDetailView.as_view()),
    path('publisherlist/', list, name="list")
]
