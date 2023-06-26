from django.urls import path
from .views import index, all_api, add_api, remove_api, filter_api

urlpatterns = [
    path('', index),
    path('all_api', all_api),
    path('add_api', add_api),
    path('remove_api', remove_api),
    path('remove_api/<int:emp_id>', remove_api),
    path('filter_api', filter_api),
]