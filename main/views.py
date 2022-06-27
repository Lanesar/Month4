from django.shortcuts import render
from main.models import Product, Category, Movie, Movie_Rev, Director

# Create your views here.


def index(request):
    dict_ = {
        'key': 'Hello World',
        'color': 'yellow',
        'list_': ['Abylai', "Salima", "Sanjar", 'Janat']
    }
    return render(request, 'index.html', context=dict_)


def product_list_view(request):
    #    products = Product.objects.all()   QuerySet
    context = {
        'Product_list': Product.objects.all(),
        'Category_list': Category.objects.all()
    }

    return render(request, 'products.html', context=context)


def main(req):
    return render(req, 'main.html')


def dt(r):
    return render(r, 'dtime.html')


def info(a):
    return render(a, 'info.html')


def product_detail_view(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'detail.html', context={'Product_detail': product,
                                                   'Category_list': Category.objects.all()})


def category_product_filter_view(request, category_id):
    context = {
        'Product_list': Product.objects.filter(category_id=category_id),
        'Category_list': Category.objects.all()
    }
    return render(request, 'products.html', context=context)


def movies(request):
    movies = Movie.objects.all()
    return render(request, 'movies.html', context={'movies': movies})


def movies_view(request, id):
    movie_list = {
        'Movie': Movie.objects.filter(id=id),
        'Reviews': Movie_Rev.objects.filter(Movie_id=id)
    }
    return render(request, 'detail_movies.html', context=movie_list)


def directors(request):
    Directors = Director.objects.all()
    return render(request, 'directors.html', context={'directors': Directors})


def director_view(request, id):
    Director_ = Director.objects.get(id=id)
    return render(request, 'director.html', context={'director': Director_})


def reviews(request):
    Reviews = Movie_Rev.objects.all()
    return render(request, 'reviews.html', context={'reviews': Reviews})


def reviews_view(request, id):
    review = Movie_Rev.objects.get(id=id)
    return render(request, 'review_view.html', context={'review': review})







