from django.contrib import admin
from django.urls import path, include

from .views import CenterListView, CenterDetailsView

urlpatterns = [
    path('',CenterListView.as_view(), name = 'centers'),
    path('<int:pk>/',CenterDetailsView.as_view(), name = 'center_details'),
]
