from django.contrib import admin
from .models import Category, CategoryImage, Product, ProductImage,Carousel,CarouselImage

# Inline for Category images
class CategoryImageInline(admin.TabularInline):
    model = CategoryImage
    extra = 1  # empty image form by default

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date']
    inlines = [CategoryImageInline]

    # Inline for Carousel images
class CarouselImageInline(admin.TabularInline):
    model = CarouselImage
    extra = 1  # empty image form by default

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['text', 'created_date']
    inlines = [CarouselImageInline]

# Inline for Product images
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'created_date']
    inlines = [ProductImageInline]
