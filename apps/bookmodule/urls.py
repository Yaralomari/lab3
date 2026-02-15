from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='book_index'),
    path('index2/<val1>/', views.index2, name='book_index2'),

    # Task 7
    path('<int:bookId>', views.viewbook),
]