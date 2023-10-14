from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to="images/categories", blank=False, null=False)
    banner = models.ImageField(upload_to="images/categories/banner", blank=False, null=False)

    class Meta:
        verbose_name = ('category')
        verbose_name_plural = ('categories')

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.name