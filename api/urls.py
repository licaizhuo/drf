from django.urls import path

from api import views

urlpatterns = [
    path('test/', views.TestAPIView.as_view()),
    path('test/<str:id>/', views.TestAPIView.as_view()),
    path('tt/', views.TestPermissionAPIView.as_view()),
    path('ul/', views.UserLoginOrReadOnly.as_view()),
    path('sm/', views.SendMessageAPIView.as_view()),
]
