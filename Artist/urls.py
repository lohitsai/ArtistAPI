from django.urls import path, include
from Artist.views import ArtistList, RegisterUser, LoginUser

urlpatterns = [
    path("artists/", ArtistList.as_view()),
    path("register/", RegisterUser.as_view()),
    path("login/", LoginUser.as_view()),
]
