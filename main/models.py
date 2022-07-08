from django.db import models
from django.utils.html import mark_safe


# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Rejiser'
        verbose_name_plural = 'Rejiseri'

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='movies', null=True)

    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Filmi'

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 300px;" />' % self.image.url)
        else:
            return mark_safe('<img src="https://png.pngtree.com/element_our/20190531/ourmid/pngtree-gray-cross-symbol-free-illustration-image_1280885.jpg"'
                             'style="width: 300px"')
    image_tag.short_description = 'Image'


class Movie_Rev(models.Model):
    text = models.TextField()
    Movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Otziv filma'
        verbose_name_plural = 'Otzivi filma'

    def __str__(self):
        return self.text


class Category(models.Model):
    class Meta:
        verbose_name = 'kategoriya'
        verbose_name_plural = 'kategorii'

    name = models.CharField('Imya', max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    class Meta:
        verbose_name = 'teg'
        verbose_name_plural = 'tegi'

    name = models.CharField('imya', max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'tovar'
        verbose_name_plural = 'tovari'

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='categoriya')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='tegi')
    name = models.CharField(max_length=1000, verbose_name='imya')  # names
    description = models.TextField(blank=True,
                                   verbose_name='opisaniya')  # lorem ipsum blank true refers to the admin page
    price = models.FloatField(verbose_name='cena v dollarah')  # 199.9
    #    quantity = models.IntegerField()  # 100
    is_active = models.BooleanField(default=True, verbose_name='activen?')  # True or False
    created_at = models.DateTimeField(auto_now_add=True)  # 2022-06-06
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products', null=True, verbose_name='kartinka')

    def __str__(self):
        return self.name

    @property
    def tags_list(self):
        return ', '.join([tag.name for tag in self.tags.all()])


class Review(models.Model):
    class Meta:
        verbose_name = 'otziv'
        verbose_name_plural = 'otzivi'

    text = models.TextField(verbose_name='tekst')
    author = models.CharField(max_length=100, null=True, blank=True, default='', verbose_name='avtor')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', verbose_name='produkt')

    def __str__(self):
        return self.text
