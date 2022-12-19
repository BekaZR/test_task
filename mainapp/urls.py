from django.urls import path
from rest_framework.routers import DefaultRouter as DR

from mainapp.views import EntityView, PropertyView, post


router = DR()

router.register("properties", PropertyView, basename="properties")
router.register("entity", EntityView, basename="entity")

urlpatterns = [
    path("entity_wrong_data/", post)
]

urlpatterns += router.urls