from django.urls import path
from .views import *

app_name= 'post'

urlpatterns = [
    path('', frontpage, name= 'frontpage'),
    path('caregory/<slug:slug>/',caregory_detail, name= 'caregory_detail'),
    path('post/<slug:slug>/', post_detail, name= 'post_detail'),
]