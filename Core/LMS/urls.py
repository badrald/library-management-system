from django.urls import path
from . import views

urlpatterns=[
    path('',views.Index,name='mangment'),
    path('books/',views.Books,name='mang_books'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('profiles/',views.profiles,name='profiles'),
    path('delete_user/<int:id>',views.delete_user,name='delete_user'),
    path('upgrade_user/<int:id>',views.givePermission,name='givePermission'),
    path('downgrade_user/<int:id>',views.takePermission,name='takePermission')

]