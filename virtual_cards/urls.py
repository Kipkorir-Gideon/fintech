from django.urls import path
from .views import VirtualCardCreateView

urlpatterns = [
    path('create-card/', VirtualCardCreateView.as_view(), name='create_virtual_card'),
]