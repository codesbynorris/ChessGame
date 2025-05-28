from django.urls import path
from .views import get_best_move

urlpatterns = [
    path('get-best-move/', get_best_move, name='get_best_move'),
]
