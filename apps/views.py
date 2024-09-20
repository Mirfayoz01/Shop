from django.views.generic import ListView, TemplateView
from apps.models import Product



class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product.html'


class RegisterView(TemplateView):
    template_name = 'register.html'

class LoginView(TemplateView):
    template_name = 'login.html'