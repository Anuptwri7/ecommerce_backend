from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field, OpenApiTypes
from .models import Category, CategoryImage, Product, ProductImage,Carousel,CarouselImage

# ---------------- CATEGORY ----------------
class CategoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryImage
        fields = ['id', 'image']

class CategorySerializer(serializers.ModelSerializer):
    # File upload for new images
    images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )
    # For GET requests
    images_url = CategoryImageSerializer(source='images', many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'created_date', 'images', 'images_url']

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        category = Category.objects.create(**validated_data)
        for img in images_data:
            CategoryImage.objects.create(category=category, image=img)
        return category

    def update(self, instance, validated_data):
        images_data = validated_data.pop('images', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        for img in images_data:
            CategoryImage.objects.create(category=instance, image=img)
        return instance

# ---------------- PRODUCT ----------------
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']

class ProductSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )
    images_url = ProductImageSerializer(source='images', many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'description', 'price', 'created_date', 'images', 'images_url']

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        product = Product.objects.create(**validated_data)
        for img in images_data:
            ProductImage.objects.create(product=product, image=img)
        return product

    def update(self, instance, validated_data):
        images_data = validated_data.pop('images', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        for img in images_data:
            ProductImage.objects.create(product=instance, image=img)
        return instance
    
    # ---------------- Carousel ----------------
from rest_framework import serializers
from .models import Carousel, CarouselImage


class CarouselImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarouselImage
        fields = ['id', 'image']


class CarouselSerializers(serializers.ModelSerializer):
    # 🔹 READ: return images in response
    images_url = CarouselImageSerializers(
        source='images',
        many=True,
        read_only=True
    )

    # 🔹 WRITE: upload multiple images
    images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Carousel
        fields = [
            'id',
            'text',
            'created_date',
            'images_url',  # 👈 RETURNED in GET
            'images'       # 👈 USED only in POST
        ]

    def create(self, validated_data):
        images = validated_data.pop('images', [])
        carousel = Carousel.objects.create(**validated_data)

        for image in images:
            CarouselImage.objects.create(
                carousel=carousel,
                image=image
            )

        return carousel



