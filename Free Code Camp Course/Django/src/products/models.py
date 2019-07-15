from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    summary = models.TextField(default='This is cool!')
    featured = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"id": self.id})  # f"/product/{self.id}"
