from rest_framework import serializers

from characters.models import Characters


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characters
        fields = "__all__"
