from django.urls import path

from app_autiste.vues.users.v_users import LoginView, LogoutView, RegisterView, UserView


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
]