import random

from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from characters.models import Characters
from characters.serializers import CharacterSerializer


@extend_schema(responses={status.HTTP_200_OK: CharacterSerializer})
@api_view(["GET"])
def get_random_character(request: Request) -> Response:
    """Get a random character."""
    pks = Characters.objects.values_list("pk", flat=True)
    random_pk = random.choice(pks)
    random_character = Characters.objects.get(pk=random_pk)
    serializer = CharacterSerializer(random_character)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CharacterListView(generics.ListAPIView):
    serializer_class = CharacterSerializer
    queryset = Characters.objects.all()

    def get_queryset(self):
        queryset = Characters.objects.all()
        name = self.request.query_params.get("name")
        if name:
            return queryset.filter(name__icontains=name)
        return queryset

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="name",
                description="Filter by characters ex(?name=Rick)",
                type=str,
                required=True,
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
