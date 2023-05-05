from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_crop, name='add_crop'),
    path('<int:crop_id>/', views.crop_detail, name='crop_detail'),
    path('crop/', views.crop_list, name='crop_list'),
    path('crop_statistics/', views.crop_statistics, name='crop_statistics'),

]
