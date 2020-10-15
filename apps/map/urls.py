"""Manage folium package related routes."""
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('ajax/create-marker/', csrf_exempt(views.create_marker)),
    path('ajax/getMarkers/', csrf_exempt(views.getAllMarkers)),
    path('ajax/categories/', csrf_exempt(views.categories)),
    path('ajax/search/', csrf_exempt(views.search)),
    path('ajax/subcategories/', csrf_exempt(views.subcategories)),
    path('ajax/load_sub_categories/', views.MarkerUpdate.load_cities),
    path('update-marker/<int:pk>', views.MarkerUpdate.as_view(), name="update_marker"),
]
