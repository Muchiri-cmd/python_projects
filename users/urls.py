<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> aecf3b8f20cf3b4e6b08ba79e5e6ac054ba1aace
#patterns for users

from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

app_name="users"
<<<<<<< HEAD
=======
=======
#defines url patterns for users

from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name='users'
>>>>>>> feea372ff8d2b558b178edc6f857898fb38b1e6f
>>>>>>> aecf3b8f20cf3b4e6b08ba79e5e6ac054ba1aace

urlpatterns = [
    #login page
    path('login/',LoginView.as_view(template_name='users/login.html'),name='login'),
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> aecf3b8f20cf3b4e6b08ba79e5e6ac054ba1aace
    #logout
    path('logout/',views.logout_view,name='logout'),
    #Registration page
    path('register/',views.register,name='register'),
]
<<<<<<< HEAD
=======
=======
    #logout page
    path('logout/',views.logout_view,name='logout'),
    #registration page
    path('register/',views.register,name='register'),
]



>>>>>>> feea372ff8d2b558b178edc6f857898fb38b1e6f
>>>>>>> aecf3b8f20cf3b4e6b08ba79e5e6ac054ba1aace
