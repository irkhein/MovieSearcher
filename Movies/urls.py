from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Movies'

urlpatterns = [
    # /Movies/
    path('', views.IndexView.as_view(), name="index"),

    # /register/
    path('register', views.UserFormView.as_view(), name="register"),

    # /login/
    path('login', views.UserLoginFormView.as_view(), name="login"),

    # /logout/
    path('logout', views.UserLogoutView.as_view(), name="logout"),

    # /Movies/<item_id>
    path('<int:pk>', views.MovieDetailView.as_view(), name="movie"),

    # /Movies/movie/add
    path('movie/add', views.MovieCreate.as_view(), name="movie-add"),

    # /Movies/7/update
    path('movie/<int:pk>/update', views.MovieUpdate.as_view(), name="movie-update"),

    # /Movies/7/delete
    path('movie/<int:pk>/delete', views.MovieDelete.as_view(), name="movie-delete"),

    # /Movies/<item_id>/like/
    path('<int:item_id>/like', views.like_movie, name="like-movie"),

    # /Movies/<item_id>/dislike/
    path('<int:item_id>/dislike', views.dislike_movie, name="dislike-movie"),

    # /Movies/Person/<item_id>
    path('person/<int:pk>', views.PersonDetailView.as_view(), name="person"),

    # /Movies/person/<item_id>/like/
    path('person/<int:item_id>/like', views.like_person, name="like-person"),

    # /Movies/person/<item_id>/dislike/
    path('person/<int:item_id>/dislike', views.dislike_person, name="dislike-person"),

    # /Movies/7/actors
    path('movie/<int:pk>/actors', views.PersonListView.as_view(), name="actors"),
]
