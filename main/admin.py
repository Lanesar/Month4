from django.contrib import admin
from main.models import Product, Category, Tag, Review, Movie, Movie_Rev, Director
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Review)
admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Movie_Rev)

