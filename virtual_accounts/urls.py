from  django.urls import path
from .views import VirtualAccountCreateView

urlpatterns = [
    path('create-account/', VirtualAccountCreateView.as_view(), name='create_virtual_account'),
]