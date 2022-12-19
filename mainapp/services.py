from mainapp.models import Entity


def create_entity(data, user):
    entity = Entity.objects.create(
        modified_by=user,
        value=data.get("data[value]")
    )
    return entity

def to_representation(data):
    data = data.__dict__.copy()
    del data["_state"]
    return data