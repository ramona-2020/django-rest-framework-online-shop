from django.urls import path
from online_store.main_app.views import ProductListView, ListOrdersView

urlpatterns = [
    path('products/', ProductListView.as_view({'get': 'list'})),
    path('stats/', ListOrdersView.as_view({'get': 'list'})),
]
