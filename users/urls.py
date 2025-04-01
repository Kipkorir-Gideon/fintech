from django.urls import path
from .views import RegisterView, ProfileView, LoginView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),  # TODO: Add JWT authentication instead of session authentication for production.  # noqa E501
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
]