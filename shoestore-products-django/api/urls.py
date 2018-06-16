from django.conf.urls import url
from .views import ListProductsView

urlpatterns = [
    url(r'products$', ListProductsView.as_view(), name="products-all")
]