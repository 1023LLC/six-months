# from django.urls import path

# from . import views


# urlpatterns = [
#     path('list/', views.books_list),
#     path('', views.book_create),
#     path('<int:pk>/', views.book)
# ]

from django.urls import path

from .views import BookList, BookCreate, BookDetail


urlpatterns = [
    path('', BookCreate.as_view()),
    path('list/', BookList.as_view()),
    path('<int:pk>/', BookDetail.as_view())
]