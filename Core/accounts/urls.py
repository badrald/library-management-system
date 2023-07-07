from django.urls import path

from . import views

app_name='accounts'

urlpatterns = [
    path("SignUp/",views.signup_view,name='signup'),
    path("login/",views.login_view,name="login"),
    path("logout/",views.logOut,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit/',views.profile_edit,name='profile_edit'),
]
