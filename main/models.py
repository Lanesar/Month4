from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Movie_Rev(models.Model):
    text = models.TextField()
    Movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    name = models.CharField(max_length=1000)  # names
    description = models.TextField(blank=True)  # lorem ipsum blank true refers to the admin page
    price = models.FloatField()  # 199.9
#    quantity = models.IntegerField()  # 100
    is_active = models.BooleanField(default=True)  # True or False
    created_at = models.DateTimeField(auto_now_add=True)  # 2022-06-06
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100, null=True, blank=True, default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.text


