from django.urls import path
from .views import show_notes

urlpatterns = [
    path('', show_notes, name='show-notes')
]
