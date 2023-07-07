from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name='index'),
    path('book/<int:id>',views.bookDetails,name='bookDetails'),
    path("books/",views.books,name="books")
]
