"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from post.views import posts_list, posts_list_api_view, post_details, create_post, delete_post
from review.views import toggle_like, CreateCommentAPIView, UpdateCommentAPIView, DeleteCommentAPIView
from account.views import RegisterUserAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('listing/', posts_list),
    path('api/listing/', posts_list_api_view),
    path('api/details/<int:id>/', post_details),
    path('api/create/', create_post),
    path('api/delete/<int:id>/', delete_post),
    path('api/like/<int:id>/', toggle_like),
    path('api/register/', RegisterUserAPIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/comment/create/', CreateCommentAPIView.as_view()),
    path('api/comment/update/<int:pk>/', UpdateCommentAPIView.as_view()),
    path('api/comment/delete/<int:pk>/', DeleteCommentAPIView.as_view()),
]
