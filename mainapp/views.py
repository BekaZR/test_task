from rest_framework.viewsets import ModelViewSet

from mainapp.models import Property, Entity
from mainapp.serializers import EntityGetSerializer, EntitySerializer, PropertySerializer


class PropertyView(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class EntityView(ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return EntityGetSerializer
        return EntitySerializer
    
    def perform_create(self, serializer):
        serializer.save(modified_by=self.request.user)