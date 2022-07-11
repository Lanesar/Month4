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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.IndexView.as_view()),
    path('', views.Main.as_view()),
    path('dt/', views.Dt.as_view()),
    path('info/', views.Info.as_view()),
    path('products/', views.ProductListView.as_view()),
    path('products/<int:pk>/', views.ProductDetailView.as_view()),
    path('category/<int:category_id>/products/', views.CategoryProductFilterView.as_view()),
    path('movies/', views.Movies.as_view()),
    path('movies/<int:pk>/', views.MoviesDetailView.as_view()),
    path('directors/', views.Directors.as_view()),
    path('directors/<int:pk>/', views.DirectorView.as_view()),
    path('reviews/', views.Reviews.as_view()),
    path('reviews/<int:pk>/', views.ReviewView.as_view()),
    path('add_product/', views.AddProductFormView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('add_director/', views.DirectorReg.as_view()),
    path('add_movie/', views.MovieReg.as_view()),
    path('logout/', views.LogoutView.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
