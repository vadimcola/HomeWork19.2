from django.urls import path

from catalog.views import *

urlpatterns = [
    path('', home),
    path('contacts/', contacts)
]