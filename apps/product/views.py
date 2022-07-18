from apps.product.models import Category
from apps.product.serializers import CategorySerializer
from rest_framework.generics import *


# class CategoryListView(ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
#  class CategoryCreateView(CreateAPIView):
#      serializer_class = CategorySerializer
#


 # class CategoryDetailView(RetrieveAPIView):
 #     queryset = Category.objects.all()
 #     serializer_class = CategorySerializer
 #
 # class CategoryUpdateView(UpdateAPIView):
 #     queryset = Category.objects.all()
 #     serializer_class = CategorySerializer
 #
 # class CategoryDeleteView(DestroyAPIView):
 #     queryset = Category.objects.all()
 #     serializer_class = CategorySerializer

class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
