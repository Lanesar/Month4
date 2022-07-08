from django.shortcuts import render, redirect
from main.models import Product, Category, Movie, Movie_Rev, Director, Review
from main.forms import ProductForm, RegisterForm, LoginForm, DirectorForm, MovieForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView, FormView
from django.views import View
# Create your views here.


def index(request):
    dict_ = {
        'key': 'Hello World',
        'color': 'yellow',
        'list_': ['Abylai', "Salima", "Sanjar", 'Janat']
    }
    return render(request, 'index.html', context=dict_)


class IndexView(View):
    def get(self, request):
        dict_ = {
            'key': 'Hello World',
            'color': 'yellow',
            'list_': ['Abylai', "Salima", "Sanjar", 'Janat']
        }
        return render(request, 'index.html', context=dict_)

    def post(self, request):
        pass


def product_list_view(request):
    #    products = Product.objects.all()   QuerySet
    context = {
        'Product_list': Product.objects.all(),
        'Category_list': Category.objects.all()
    }

    return render(request, 'products.html', context=context)


class ContextData:
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['Category_list'] = Category.objects.all()
        return context


class ProductListView(ContextData, ListView):
    queryset = Product.objects.all()
    template_name = 'products.html'
    context_object_name = 'Product_list'


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


class ProductDetailView(ContextData, DetailView):
    model = Product
    template_name = 'detail.html'
    context_object_name = 'Product_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['reviews'] = Review.objects.filter(product=self.object)
        return context


def category_product_filter_view(request, category_id):
    context = {
        'Product_list': Product.objects.filter(category_id=category_id),
        'Category_list': Category.objects.all()
    }
    return render(request, 'products.html', context=context)


class CategoryProductFilterView(ContextData, ListView):
    queryset = Product.objects.all()
    template_name = 'products.html'
    context_object_name = 'Product_list'

    def get_queryset(self):
        return Product.objects.filter(category_id=self.request.resolver_match.kwargs['category_id'])


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


class AddProductFormView(ContextData, FormView):
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = '/products/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def add_product_view(request):
    form = ProductForm()
#    print(request.POST)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products/')
    return render(request, 'add_product.html', context={
            'form': form,
            'Category_list': Category.objects.all()
    })


def director_reg(request):
    form = DirectorForm()
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/directors/')
    return render(request, 'director_reg.html', context={
            'form': form
    })


def movie_reg(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/movies/')
    return render(request, 'movie_reg.html', context={
            'form': form
    })


def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    return render(request, 'register.html', context={
        'form': form
    })


def login_view(request):
    form = LoginForm
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user=user)
            return redirect('/login/')
    return render(request, 'login.html', context={
        'form': form
    })


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/login/')

