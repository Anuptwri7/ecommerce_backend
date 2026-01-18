from django.db import models

# ---------------- CATEGORY ----------------
class Category(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CategoryImage(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='images',  # Access via category.images.all()
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return f"{self.category.name} - Image {self.id}"
    

# ---------------- Carousel ----------------
class Carousel(models.Model):
    text = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class CarouselImage(models.Model):
    Carousel = models.ForeignKey(
        Carousel,
        related_name='images', 
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='carousel/')

    def __str__(self):
        return f"{self.Carousel.text} - Image {self.id}"    


# ---------------- PRODUCT ----------------
class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='images',  # Access via product.images.all()
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f"{self.product.name} - Image {self.id}"
