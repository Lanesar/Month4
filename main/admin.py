from django.contrib import admin
from main.models import Product, Category, Tag, Review, Movie, Movie_Rev, Director
from django.utils.html import format_html
# Register your models here.


class ReviewAdminInline(admin.StackedInline):
    model = Review
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = 'name tags_list category price is_active created_at updated_at'.split()
    search_fields = 'name description'.split()
    list_filter = 'category tags is_active created_at'.split()
    list_editable = 'category price is_active'.split()
    readonly_fields = 'created_at updated_at'.split()
    list_per_page = 3
    inlines = [ReviewAdminInline]


class MovieAdmin(admin.ModelAdmin):
    model = Movie
    search_fields = 'title'.split()
    list_display = 'image_tag title director'.split()
    list_filter = 'director'.split()
    readonly_fields = ('image_tag',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Review)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Director)
admin.site.register(Movie_Rev)

