from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Producto(models.Model):
    title = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    description = models.TextField()
    # imgage = models.ImageField(upload_to="images/", null=True, blank=True)
    created_at = models.DateField()
    stock = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    def __str__(self):
        return f"{self.id} - {self.title} - {self.brand} -{self.description} - {self.price} - {self.stock} - {self.created_at}"


class Review(models.Model):
    validations = [
        MinValueValidator(0, message="El valor del rating no puede ser menor que 0."),
        MaxValueValidator(5, message="El valor del rating no puede ser mayor que 5."),
    ]

    rating = models.IntegerField(validators=validations)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} - {self.rating} - {self.description} - {self.created_at} - {self.username}"

class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.id} - {self.title} - {self.description}"
