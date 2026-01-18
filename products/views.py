from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from .models import Category, Product,Carousel
from .serializers import CategorySerializer, ProductSerializer,CarouselSerializers

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @extend_schema(
        request=CategorySerializer,
        description="Create or update a Category with multiple image uploads"
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class CarouselViewSet(viewsets.ModelViewSet):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializers

    @extend_schema(
        request=CarouselSerializers,
        description="Create or update a Category with multiple image uploads"
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @extend_schema(
        request=ProductSerializer,
        description="Create or update a Product with multiple image uploads"
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
