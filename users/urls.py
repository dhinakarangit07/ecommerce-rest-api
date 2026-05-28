from django.urls import path
from .views import RegisterAPIView, LoginAPIView
from .views import users_list

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),

    path('list/', users_list, name='users-list'),
]