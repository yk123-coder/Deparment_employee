

from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('', views.index, name='home'),  
]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='home'),
# ]

