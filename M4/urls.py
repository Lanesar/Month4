"""M4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.index),
    path('', views.main),
    path('dt/', views.dt),
    path('info/', views.info),
    path('products/', views.product_list_view),
    path('products/<int:id>/', views.product_detail_view),
    path('category/<int:category_id>/products/', views.category_product_filter_view),
    path('movies/', views.movies),
    path('movies/<int:id>/', views.movies_view),
    path('directors/', views.directors),
    path('directors/<int:id>/', views.director_view),
    path('reviews/', views.reviews),
    path('reviews/<int:id>/', views.reviews_view)

]
