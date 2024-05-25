from django.urls import path
from .views import CreateProductView, ShowProductView

urlpatterns = [
    path('list/', ShowProductView.as_view()),
    path('create/', CreateProductView.as_view()),
]
