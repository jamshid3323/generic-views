from django.urls import path
from .views import *

urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    path('', BookView.as_view(), name='object'),
    path('create/', CreateBookView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateBookView.as_view(), name='update'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='delete')
]