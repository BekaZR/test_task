from django.urls import path
from rest_framework.routers import DefaultRouter as DR

from mainapp.views import EntityView, PropertyView


router = DR()

router.register("properties", PropertyView, basename="properties")
router.register("entity", EntityView, basename="entity")

urlpatterns = [
    
]

urlpatterns += router.urls