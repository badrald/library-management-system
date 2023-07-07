from django.urls import path
from . import views

urlpatterns=[
    path('',views.Index,name='mangment'),
    path('books/',views.Books,name='mang_books'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete')
]