from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from mainapp.models import Property, Entity
from mainapp.serializers import (
    EntityGetSerializer, EntitySerializer, PropertySerializer
    )
from mainapp.services import create_entity, to_representation


class PropertyView(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class EntityView(ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return EntityGetSerializer
        return EntitySerializer
    
    def perform_create(self, serializer):
        serializer.save(modified_by=self.request.user)


@api_view(["POST",])
@permission_classes([IsAuthenticated,])
def post(request):
    entity_db = create_entity(request.data, request.user)
    entity = to_representation(entity_db)
    return Response(entity)
