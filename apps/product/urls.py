from django.urls import path
from apps.product.views import *

urlpatterns = [
    path('', CategoryListCreateView.as_view()),
    path('<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view()),


    # path('',CategoryListView.as_view()),
    # path('create/', CategoryCreateView),
    # path('detail/<int:pk>/', CategoryDetailView),
    # path('update/<int:pk>/',CategoryUpdateView),
    # path('delete/<int:pk>/', CategoryDeleteView)

]