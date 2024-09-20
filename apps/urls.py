from django.urls import path
from .views import ProductListView, RegisterView, LoginView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
]