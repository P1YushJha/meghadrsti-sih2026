from django.urls import path
from .views import homePage, landingPage, loginPage, logoutUser, profilePage, registerPage

urlpatterns = [
    path('', landingPage, name="landing"),
    path('home/', homePage, name="home"),
    path('login/', loginPage, name="login"),
    path('signup/', registerPage, name="signup"),
    path('logout/', logoutUser, name="logoutUser"),
    path('profile/', profilePage, name="profile"),
]