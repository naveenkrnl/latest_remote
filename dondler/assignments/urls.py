from django.urls import path,include
from .views import submit_assignment,create_assignment

urlpatterns = [
    path('<id>/submit/', submit_assignment),
    path('assignment/create/', create_assignment),

]

