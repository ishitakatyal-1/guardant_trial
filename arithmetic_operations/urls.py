from django.urls import path
from arithmetic_operations.views import index

app_name = 'arithmetic_operations'

urlpatterns = [
    path('', index, name='index')
]
