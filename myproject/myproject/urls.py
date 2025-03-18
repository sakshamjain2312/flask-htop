
from django.urls import path
from myapp.views import htop

urlpatterns = [
    path('htop/', htop),
]

