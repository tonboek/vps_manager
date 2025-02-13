from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vps.views import VPSListCreateView, VPSDetailView, index_page

urlpatterns = [
    path('', index_page),
	path('vps/', VPSListCreateView.as_view(), name='vps-list-create'),
	path('vps/<uuid:uid>/', VPSDetailView.as_view(), name='vps-detail'),
]